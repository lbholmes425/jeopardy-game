let currentClueValue = 0;
let currentRound = "round_1";

document.addEventListener('DOMContentLoaded', () => {
    // Any init logic
});

function changeGame(gameId) {
    window.location.href = `/?game_id=${gameId}`;
}

const SOUNDS = {
    daily_double: 'https://www.myinstants.com/media/sounds/daily-double.mp3',
    board_fill: 'https://www.myinstants.com/media/sounds/jeopardy-board-fill.mp3', // Placeholder / generic harp
    think_music: 'https://www.myinstants.com/media/sounds/jeopardy-theme-song.mp3',
    times_up: 'https://www.myinstants.com/media/sounds/times-up.mp3'
};

function playSound(name) {
    if (SOUNDS[name]) {
        const audio = new Audio(SOUNDS[name]);
        audio.play().catch(e => console.error("Audio play failed", e));
        return audio;
    }
}

let activeThinkMusic = null;

function switchRound(roundId) {
    document.querySelectorAll('.board-grid, .final-round').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.round-controls button').forEach(el => el.classList.remove('active'));

    const target = document.getElementById(roundId);
    if (target) {
        target.style.display = (roundId === 'final_jeopardy') ? 'block' : 'grid';
    }

    currentRound = roundId;

    // Update active button state
    if (roundId === 'round_1') document.getElementById('btn-r1').classList.add('active');
    if (roundId === 'round_2') document.getElementById('btn-r2').classList.add('active');
    if (roundId === 'final_jeopardy') document.getElementById('btn-fj').classList.add('active');

    if (roundId !== 'final_jeopardy') {
        playSound('board_fill');
    }
}

function showClue(round, cat, index) {
    const questions = GAME_DATA[round][cat];
    const q = questions[index];

    if (!q) return;

    currentClueValue = q.value;

    const modal = document.getElementById('clue-modal');
    document.getElementById('modal-cat-name').innerText = cat;
    document.getElementById('modal-clue-text').innerText = q.clue;
    document.getElementById('modal-answer-text').style.display = "none";
    document.getElementById('modal-answer-text').innerText = q.answer;
    document.getElementById('show-answer-btn').style.display = "block";

    const dd = document.getElementById('daily-double-notice');
    // Daily Double Logic
    if (q.daily_double) {
        dd.style.display = "block";
        playSound('daily_double');
    } else {
        dd.style.display = "none";
    }

    // Media Handling
    const clueTextEl = document.getElementById('modal-clue-text');
    const mediaContainer = document.getElementById('modal-media-container');

    // Clear previous media
    if (mediaContainer) {
        mediaContainer.innerHTML = '';
        mediaContainer.style.display = 'none';
    }

    // Handle Media Types
    if (q.type === 'image') {
        mediaContainer.style.display = 'block';
        const img = document.createElement('img');
        img.src = q.url;
        img.className = 'clue-media';
        mediaContainer.appendChild(img);
    } else if (q.type === 'video') {
        mediaContainer.style.display = 'block';
        const vid = document.createElement('video');
        vid.src = q.url;
        vid.className = 'clue-media';
        vid.controls = true;
        vid.autoplay = true;
        mediaContainer.appendChild(vid);
    } else if (q.type === 'audio') {
        // ... audio logic if needed
    }

    modal.style.display = 'block';

    // Mark as used
    // Need to handle spaces in IDs
    const safeCat = cat.replace(/ /g, '-');
    const cellId = (round === 'round_1' ? 'r1' : 'r2') + '-' + safeCat + '-' + index;
    const cell = document.getElementById(cellId);
    if (cell) cell.classList.add('used');
}

function revealAnswer() {
    document.getElementById('modal-answer-text').style.display = "block";
    document.getElementById('show-answer-btn').style.display = "none";
}

function closeModal() {
    document.getElementById('clue-modal').style.display = 'none';
}

function updateScore(teamId, amount) {
    const scoreEl = document.getElementById(`score-${teamId}`);
    let current = parseInt(scoreEl.innerText);
    current += amount;
    scoreEl.innerText = current;
}

function awardPoints(teamId) {
    updateScore(teamId, currentClueValue);
    closeModal();
}

function deductPoints(teamId) {
    updateScore(teamId, -currentClueValue);
    // Do NOT close modal, allow other teams to guess or show answer
}

function showFinalClue() {
    // Reuse modal logic or custom view for Final Jeopardy
    const q = GAME_DATA.final_jeopardy;
    currentClueValue = 0; // Usually wagered, so we won't auto-add

    const modal = document.getElementById('clue-modal');
    document.getElementById('modal-cat-name').innerText = q.category;
    document.getElementById('modal-clue-text').innerText = q.clue;
    document.getElementById('modal-answer-text').style.display = "none";
    document.getElementById('modal-answer-text').innerText = q.answer;
    document.getElementById('show-answer-btn').style.display = "block";
    document.getElementById('daily-double-notice').style.display = "none";

    // Clear media
    const mediaContainer = document.getElementById('modal-media-container');
    if (mediaContainer) {
        mediaContainer.innerHTML = '';
        mediaContainer.style.display = 'none';
    }

    modal.style.display = 'block';

    activeThinkMusic = playSound('think_music');
}

// Close modal if clicking outside content
window.onclick = function (event) {
    const modal = document.getElementById('clue-modal');
    if (event.target == modal) {
        closeModal();
    }
}

// Ensure music stops on close
const originalCloseModal = closeModal;
closeModal = function () {
    originalCloseModal();
    if (activeThinkMusic) {
        activeThinkMusic.pause();
        activeThinkMusic.currentTime = 0;
        activeThinkMusic = null;
    }
}
