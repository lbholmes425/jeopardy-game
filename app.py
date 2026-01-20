from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room
from game_data import GAMES
from copy import deepcopy
import random
import os
import json
import glob

# --- Load External Games ---
from pyngrok import ngrok
import sys

# --- Networking Helper ---
public_tunnel_url = None

def start_ngrok():
    """Starts an Ngrok tunnel and returns the public URL."""
    try:
        # Check if we have an auth token (optional but recommended)
        # ngrok.set_auth_token("YOUR_TOKEN") 
        
        # Open a HTTP tunnel on the default port 5001
        # We specify the port directly
        public_url = ngrok.connect(5001).public_url
        print(f" * Ngrok Tunnel Started: {public_url}")
        return public_url
    except Exception as e:
        print(f" * Ngrok Error: {e}")
        return None

def get_base_url():
    """Returns the best available URL (Ngrok, Cloud, or Local IP)."""
    # 1. Try Ngrok (Dev Mode)
    global public_tunnel_url
    if public_tunnel_url:
        return public_tunnel_url

    # 2. Try Render Environment Variable (Most Reliable for Cloud)
    if os.environ.get('RENDER_EXTERNAL_HOSTNAME'):
        return f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}"
    
    # 3. Try Flask Request Context (Production / standard access)
    # This automatically handles whatever domain the user is visiting (localhost, render.com, etc)
    if request:
        return request.url_root.rstrip('/')

    # 4. Fallback to reliable Local IP if outside request context
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return f"http://{ip}:5001"
    except:
        return "http://127.0.0.1:5001"


def load_external_games():
    game_dir = os.path.join(os.path.dirname(__file__), 'games')
    if not os.path.exists(game_dir):
        return

    for filepath in glob.glob(os.path.join(game_dir, '*.json')):
        try:
            with open(filepath, 'r') as f:
                game_data = json.load(f)
                # Expecting structure: { "game_id": { ... game data ... } }
                # Or just the game object and we deduce ID?
                # Let's assume the file *contains* the game object and the filename is the ID?
                # Or the file contains a dict of games (likely just one).
                # Implementation Plan said "scan games/ directory".
                # Let's support: filename "week_01.json" -> key "week_01", content is the value.
                game_id = os.path.splitext(os.path.basename(filepath))[0]
                GAMES[game_id] = game_data
                # Ensure title exists if not
                if 'title' not in game_data:
                    game_data['title'] = game_id.replace('_', ' ').title()
        except Exception as e:
            print(f"Error loading game {filepath}: {e}")
    
    print(f"DEBUG: Loaded {len(GAMES)} games.")
    if 'week_01' in GAMES:
        print(f"DEBUG: week_01 title is: '{GAMES['week_01'].get('title')}'")

load_external_games()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.context_processor
def inject_ip():
    return dict(base_url=get_base_url())

# Global Game State
class GameState:
    def __init__(self):
        self.game_id = 'original'
        self.game_data = None
        self.current_round = 'round_1'
        self.scores = {} # Dynamic: {team_id: score}
        self.team_names = {}
        self.current_clue = None # {round, category, index, value, question, answer}
        self.buzzer_locked = False
        self.buzzed_team = None
        self.open_clues = [] # List of IDs that have been played
        self.attempted_teams = [] # List of teams that have already buzzed for current clue
        
        # Final Jeopardy State
        self.final_phase = None # 'wager', 'answer', 'reveal'
        self.final_clue_text = None 
        self.final_wagers = {} # {team_id: amount}
        self.final_answers = {} # {team_id: answer_text}
        self.final_reveal_state = {} # {team_id: {'wager': bool, 'answer': bool}}
        self.active_teams = [] # List of joined team IDs

    def load_game(self, game_id):
        if game_id not in GAMES:
            game_id = 'original'
        self.game_id = game_id
        # Deep copy to allow mutation (like daily doubles) without ruining master
        self.game_data = deepcopy(GAMES[game_id])
        self.assign_daily_doubles()
        self.open_clues = []
        self.current_round = 'round_1'
        # Reset scores dynamically
        self.scores = {}
        self.buzzer_locked = False
        self.buzzed_team = None
        self.attempted_teams = []
        
        # Reset FJ
        self.final_phase = None
        self.final_clue_text = None
        self.final_wagers = {}
        self.final_answers = {}
        self.final_reveal_state = {}
        
        # Reset DD
        self.dd_state = None
        self.dd_team = None
        self.dd_wager = 0
        
        # Reset active teams and names
        self.active_teams = []
        self.team_names = {}

    def assign_daily_doubles(self):
        # same logic as before
        def pick(round_key, count):
            pool = []
            if round_key not in self.game_data: return
            for cat, qs in self.game_data[round_key].items():
                for i in range(len(qs)):
                    qs[i]["daily_double"] = False
                    pool.append((cat, i))
            count = min(count, len(pool))
            for cat, i in random.sample(pool, count):
                self.game_data[round_key][cat][i]["daily_double"] = True
        
        pick("round_1", 1)
        pick("round_2", 2)

STATE = GameState()
STATE.load_game('original')

# Helper functions for routes
def _get_public_state():
    # This function should return a dictionary of the game state that is safe to expose to clients.
    # It should NOT include sensitive information like correct answers.
    public_state = {
        'game_id': STATE.game_id,
        'current_round': STATE.current_round,
        'scores': STATE.scores,
        'team_names': STATE.team_names,
        'current_clue': STATE.current_clue, # This will be sanitized before sending to players
        'buzzer_locked': STATE.buzzer_locked,
        'buzzed_team': STATE.buzzed_team,
        'open_clues': STATE.open_clues,
        'attempted_teams': STATE.attempted_teams,
        'final_phase': STATE.final_phase,
        'final_clue_text': STATE.final_clue_text,
        'final_wagers': STATE.final_wagers,
        'final_answers': STATE.final_answers,
        'final_reveal_state': STATE.final_reveal_state,
        'active_teams': STATE.active_teams,
        'dd_state': STATE.dd_state,
        'dd_team': STATE.dd_team,
        'dd_wager': STATE.dd_wager,
        'game_title': GAMES.get(STATE.game_id, {}).get('title', 'Unknown Game')
    }
    
    # Sanitize current_clue for public view (remove answer)
    if public_state['current_clue']:
        sanitized_clue = public_state['current_clue'].copy()
        if 'answer' in sanitized_clue:
            del sanitized_clue['answer']
        public_state['current_clue'] = sanitized_clue
        
    return public_state

def format_game_list():
    return [{"id": k, "title": v["title"]} for k, v in GAMES.items()]

def get_current_game():
    return STATE.game_data

# --- Routes ---

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/host_login', methods=['GET', 'POST'])
def host_login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == '1234': # Simple password for now
            session['is_host'] = True
            return redirect(url_for('host_view'))
        else:
            return render_template('host_login.html', error="Invalid Password")
    return render_template('host_login.html')

@app.route('/host')
def host_view():
    if not session.get('is_host'):
        return redirect(url_for('host_login'))
    game_list = [{"id": k, "title": v["title"]} for k, v in GAMES.items()]
    return render_template("host.html", game=STATE.game_data, state=_get_public_state(), game_list=game_list)

@app.route('/board')
def board_view():
    return render_template("board.html", game=STATE.game_data, state=_get_public_state())

@app.route("/join")
def join_view():
    return render_template("player.html", state=_get_public_state())

# --- Socket Events ---

@socketio.on('connect')
def on_connect():
    print('Client connected')
    # Send current state to new client
    emit('state_update', _get_public_state())

@socketio.on('host_action')
def handle_host_action(data):
    action = data.get('action')
    
    if action == 'load_game':
        STATE.load_game(data.get('game_id'))
        # Reset names on load? Maybe
        STATE.team_names = {}
        STATE.active_teams = []
        emit('game_loaded', _get_public_state(), broadcast=True)
    
    elif action == 'switch_round':
        STATE.current_round = data.get('round')
        STATE.current_clue = None # Close any open question
        STATE.attempted_teams = []
        
        # FJ Logic
        if STATE.current_round == 'final_jeopardy':
            STATE.final_phase = 'wager'
            STATE.final_wagers = {}
            STATE.final_answers = {}
            STATE.final_reveal_state = {t: {'wager': False, 'answer': False} for t in STATE.active_teams}
            
            # Load Clue Text
            fj = STATE.game_data.get('final_jeopardy', {})
            STATE.final_clue_text = fj.get('clue', 'No Clue Found')
        
        # Reset DD
        STATE.dd_state = None
        STATE.dd_team = None
        
        emit('round_switched', {'round': STATE.current_round}, broadcast=True)
        emit('state_update', _get_public_state(), broadcast=True)

    elif action == 'join_team':
        team = int(data.get('team'))
        name = data.get('name')
        if team not in STATE.active_teams:
            STATE.active_teams.append(team)
            STATE.active_teams.sort()
            if team not in STATE.scores:
                STATE.scores[team] = 0
        if name:
            STATE.team_names[team] = name
            
        emit('state_update', _get_public_state(), broadcast=True)

    elif action == 'open_clue':
        # r = round, c = category, i = index
        r, c, i = data.get('round'), data.get('category'), data.get('index')
        
        try:
            clue_obj = STATE.game_data[r][c][i]
        except KeyError as e:
            print(f"ERROR: open_clue failed. Round: {r}, Cat: {c}, Index: {i}")
            print(f"Available Categories in {r}: {list(STATE.game_data.get(r, {}).keys())}")
            return
        except TypeError as e:
            print(f"ERROR: structure mismatch in open_clue. Data: {STATE.game_data.get(r, {}).get(c)}")
            return
        
        is_dd = clue_obj.get('daily_double', False)
        
        STATE.current_clue = {
            'round': r, 'category': c, 'index': i,
            'value': clue_obj['value'],
            'clue': clue_obj['clue'],
            'answer': clue_obj['answer'],
            'type': clue_obj.get('type', 'text'),
            'url': clue_obj.get('url'),
            'daily_double': is_dd
        }
        STATE.buzzer_locked = True # Default lock
        STATE.buzzed_team = None
        STATE.attempted_teams = []
        
        # Add to used list
        clue_id = f"{r}-{c.replace(' ', '-')}-{i}"
        if clue_id not in STATE.open_clues:
            STATE.open_clues.append(clue_id)

        if is_dd:
            STATE.dd_state = 'select_team'
            STATE.dd_team = None
            STATE.dd_wager = 0
            # Don't unlock buzzer
            emit('daily_double_triggered', {}, broadcast=True)
        else:
            STATE.buzzer_locked = False
            
        emit('clue_opened', STATE.current_clue, broadcast=True)
        emit('state_update', _get_public_state(), broadcast=True)

    elif action == 'close_clue':
        STATE.current_clue = None
        STATE.buzzer_locked = False
        STATE.buzzed_team = None
        STATE.attempted_teams = []
        STATE.dd_state = None
        emit('clue_closed', {}, broadcast=True)
        emit('state_update', _get_public_state(), broadcast=True)

    elif action == 'update_score':
        team = int(data.get('team'))
        delta = int(data.get('amount'))
        STATE.scores[team] += delta
        STATE.buzzer_locked = False 
        STATE.buzzed_team = None
        emit('scores_updated', STATE.scores, broadcast=True)
        
    elif action == 'dd_assign_team':
        team = int(data.get('team'))
        STATE.dd_team = team
        STATE.dd_state = 'wager'
        emit('state_update', _get_public_state(), broadcast=True)
        
    elif action == 'dd_confirm_wager':
        # Host forcing wager or player submitted?
        # Let's say player submission handles it, but host can also override?
        # Actually usually player submits.
        pass
        
    elif action == 'dd_reveal':
        STATE.dd_state = 'revealed'
        # Now host sees clue and can score
        emit('state_update', _get_public_state(), broadcast=True)
        
    elif action == 'handle_incorrect':
        team = int(data.get('team'))
        amount = int(data.get('amount')) # Negative usually
        STATE.scores[team] += amount
        
        if team not in STATE.attempted_teams:
            STATE.attempted_teams.append(team)
            
        emit('team_incorrect', {'team': team}, broadcast=True)
            
        # Re-open buzzer for others
        STATE.buzzer_locked = False
        STATE.buzzed_team = None
        
        emit('scores_updated', STATE.scores, broadcast=True)
        emit('buzzer_reset', {'attempted_teams': STATE.attempted_teams}, broadcast=True)

    elif action == 'reveal_answer':
        if STATE.current_clue:
            emit('answer_revealed', {'answer': STATE.current_clue['answer']}, broadcast=True)

    elif action == 'reset_buzzer':
        STATE.buzzer_locked = False
        STATE.buzzed_team = None
        emit('buzzer_reset', {'attempted_teams': STATE.attempted_teams}, broadcast=True)
        
    # --- Final Jeopardy Actions ---
    elif action == 'fj_start_timer':
        STATE.final_phase = 'answer'
        emit('fj_timer_started', {}, broadcast=True)
        emit('state_update', _get_public_state(), broadcast=True)
        
    elif action == 'fj_reveal_phase':
        STATE.final_phase = 'reveal'
        emit('state_update', _get_public_state(), broadcast=True)

    elif action == 'fj_reveal_item':
        team = int(data.get('team'))
        item = data.get('item') # 'wager' or 'answer'
        if team in STATE.final_reveal_state:
            STATE.final_reveal_state[team][item] = True
            emit('fj_item_revealed', {'team': team, 'item': item, 'value': STATE.final_wagers.get(team) if item == 'wager' else STATE.final_answers.get(team)}, broadcast=True)


@socketio.on('player_buzz')
def handle_buzz(data):
    team_id = data.get('team_id')
    
    # Check if team has already attempted this question
    if team_id in STATE.attempted_teams:
        return
        
    if STATE.current_clue and not STATE.buzzer_locked:
        STATE.buzzer_locked = True
        STATE.buzzed_team = team_id
        emit('buzzed_in', {'team': team_id}, broadcast=True)
        emit('buzz_timer_start', {'duration': 5}, broadcast=True)

@socketio.on('submit_wager')
def handle_wager(data):
    team_id = data.get('team_id')
    amount = int(data.get('amount', 0))
    # Validate wager <= score logic could happen here, but trusting client for now or simple cap
    current_score = STATE.scores.get(team_id, 0)
    # Allow 0 or positive, maybe allow 'all in'?
    STATE.final_wagers[team_id] = amount
    emit('wager_submitted', {'team': team_id}, broadcast=True) # Host sees who submitted

@socketio.on('submit_answer')
def handle_answer(data):
    team_id = data.get('team_id')
    text = data.get('text', '')
    STATE.final_answers[team_id] = text
    emit('answer_submitted', {'team': team_id}, broadcast=True)

@socketio.on('submit_dd_wager')
def handle_dd_wager(data):
    team_id = data.get('team_id')
    amount = int(data.get('amount', 0))
    # Validate?
    STATE.dd_wager = amount
    STATE.dd_state = 'revealed' # Auto reveal or wait? Plan said Host Reveals. 
    # Let's keep it 'wager' but maybe signal it's done? or just set wager.
    # Actually, host needs to see wager then click reveal.
    emit('state_update', _get_public_state(), broadcast=True)

def _get_public_state():
    return {
        'scores': STATE.scores,
        'current_round': STATE.current_round,
        'open_clues': STATE.open_clues,
        'current_clue': STATE.current_clue,
        'buzzed_team': STATE.buzzed_team,
        'game_id': STATE.game_id,
        'active_teams': STATE.active_teams,
        'team_names': STATE.team_names,
        # FJ State
        'final_phase': STATE.final_phase,
        'final_clue_text': STATE.final_clue_text,
        'final_wagers': STATE.final_wagers,
        'final_answers': STATE.final_answers,
        'final_reveal_state': STATE.final_reveal_state,
        'wagers_submitted': list(STATE.final_wagers.keys()),
        'answers_submitted': list(STATE.final_answers.keys()),
        # DD State
        'dd_state': STATE.dd_state,
        'dd_team': STATE.dd_team,
        'dd_state': STATE.dd_state,
        'dd_team': STATE.dd_team,
        'dd_wager': STATE.dd_wager,
        # Visual Theme
        'theme': STATE.game_data.get('theme') if STATE.game_data else None
    }

if __name__ == "__main__":
    # Start Ngrok Tunnel ONLY if locally running (not on Render/Heroku)
    # Simple check: if PORT is set, we are likely on prod.
    if not os.environ.get('PORT'):
        print(" * Starting Ngrok Tunnel...")
        public_tunnel_url = start_ngrok()
        print(f" * Game Public URL: {public_tunnel_url}")

    # Load defaults
    load_external_games()
    
    if 'week_01' in GAMES:
        STATE.load_game('week_01')
        print(" * Automatically loaded Week 01 game")
    else:
        STATE.game_data = deepcopy(GAMES.get('original', {})) # Fallback

    port = int(os.environ.get("PORT", 5001))
    # In production (when PORT is set), disable debug mode to prevent the "Werkzeug unsafe" error
    # We also pass allow_unsafe_werkzeug=True just in case it falls back to the standard server
    is_prod = bool(os.environ.get("PORT"))
    socketio.run(app, debug=not is_prod, port=port, host='0.0.0.0', allow_unsafe_werkzeug=True)
