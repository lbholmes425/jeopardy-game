import json
import os

# Define 52 Themes
THEMES = [
    ("Week 01", "New Year's Resolutions", ["Gym Failures", "Fresh Starts", "Calendar History", "Champagne Questions", "Top Hits of Last Year"]),
    ("Week 02", "Winter Wonderland", ["Snow Songs", "Ice Sports", "Cold Movies", "Hot Drinks", "Arctic Animals"]),
    ("Week 03", "Martin Luther King Jr.", ["Civil Rights", "Famous Speeches", "Peace Prize Winners", "Georgia History", "Dream Songs"]),
    ("Week 04", "Awards Season", ["Oscar Best Pictures", "Grammy Records", "Red Carpet Fashion", "Snubbed Movies", "EGOT Winners"]),
    ("Week 05", "Super Bowl Sunday", ["MVP Quarterbacks", "Halftime Shows", "Famous Commercials", "Rules of the Game", "Snack Stats"]),
    ("Week 06", "Valentine's Prep", ["Rom Com Quotes", "Famous Couples", "Chocolate Trivia", "Flower Power", "Love Ballads"]),
    ("Week 07", "Valentine's Day", ["Heart Anatomy", "St. Valentines History", "Bad Dates", "Romantic Getaways", "Kissing in Movies"]),
    ("Week 08", "Presidents Day", ["Mount Rushmore", "Presidential Pets", "First Ladies", "Executive Orders", "Currency Faces"]),
    ("Week 09", "Leap Year & Time", ["Calendar Quirks", "Time Travel Movies", "Clocks & Watches", "February History", "Longest Reigns"]),
    ("Week 10", "Oscar Night Results", ["And the Winner Is...", "Box Office Bombs", "Directors Chair", "Animated Features", "Movie Soundtracks"]),
    ("Week 11", "St. Patrick's Day", ["Green Things", "Irish History", "Leprechaun Lore", "Potatoes", "U2 & Irish Bands"]),
    ("Week 12", "March Madness", ["Cinderella Stories", "NCAA Mascots", "Bracket Busters", "Basketball Rules", "College Towns"]),
    ("Week 13", "Spring Break", ["Tropical Destinations", "Beach Movies", "Sun Safety", "Cocktails 101", "Road Trip Anthems"]),
    ("Week 14", "April Fools", ["Famous Pranks", "Comedy Movies", "Stand-up Legends", "Satire News", "Hoaxes"]),
    ("Week 15", "The Masters", ["Green Jackets", "Golf Terms", "Augusta History", "Famous Putts", "Tiger Woods"]),
    ("Week 16", "Tax Day Blues", ["Money Songs", "IRS History", "Famous Tax Evaders", "Monopoly Money", "Rich Fictional Characters"]),
    ("Week 17", "Earth Day", ["Recycling 101", "Endangered Species", "Climate Science", "Green Energy", "Nature Documentaries"]),
    ("Week 18", "Derby Days", ["Kentucky Derby", "Horse Breeds", "Famous Jockeys", "Fancy Hats", "Bourbon"]),
    ("Week 19", "Cinco de Mayo", ["Mexican History", "Tacos & Tequila", "Latin Pop Stars", "Geography of Mexico", "Spicy Foods"]),
    ("Week 20", "Mother's Day", ["TV Moms", "Famous Matriarchs", "Flower Language", "Mom Songs", "Cooking Terms"]),
    ("Week 21", "Graduation", ["Pomp & Circumstance", "Famous Valedictorians", "Ivy League", "Gap Year Travels", "Coming of Age Movies"]),
    ("Week 22", "Memorial Day", ["Military History", "BBQ Basics", "Summer Blockbusters", "Patriotic Songs", "American Flags"]),
    ("Week 23", "Summer Kickoff", ["Ice Cream Flavors", "Pool Games", "Surf Culture", "Campfire Stories", "Summer Olympics"]),
    ("Week 24", "Father's Day", ["TV Dads", "Dad Jokes", "Tools & Hardware", "BBQ Masters", "Famous Fathers"]),
    ("Week 25", "Summer Solstice", ["Sun Gods", "Longest Days", "Solar System", "Yellow Things", "Heat Waves"]),
    ("Week 26", "Halfway There", ["Midpoints", "Split Decisions", "Duos", "Hemispheres", "50% Off"]),
    ("Week 27", "Independence Day", ["Declaration Signers", "Fireworks Science", "American Revolution", "National Anthems", "States Turn 100"]),
    ("Week 28", "Shark Week", ["Shark Biology", "Jaws Trivia", "Ocean Depths", "Surfing", "Deep Blue Sea"]),
    ("Week 29", "Bastille Day", ["French Revolution", "Paris Landmarks", "French Cuisine", "Tour de France", "French Words"]),
    ("Week 30", "Summer Olympics", ["Gold Medalists", "Host Cities", "Ancient Greece", "Track & Field", "Gymnastics"]),
    ("Week 31", "Harry Potter Birthday", ["Hogwarts Houses", "Spells", "Magical Creatures", "Quidditch", "Dark Arts"]),
    ("Week 32", "Dog Days of Summer", ["Dog Breeds", "Famous TV Dogs", "Hot Weather", "Constellations", "Puppy Love"]),
    ("Week 33", "Back to School", ["School Supplies", "Classic Literature", "Geography bee", "Periodic Table", "Erasers"]),
    ("Week 34", "Labor Day", ["Unions", "Jobs TV Shows", "Career Advice", "White After Labor Day", "Working 9 to 5"]),
    ("Week 35", "NFL Kickoff", ["Super Bowl Rings", "Team Mascots", "Stadiums", "Fantasy Football", "Quarterbacks"]),
    ("Week 36", "Fall Equinox", ["Autumn Leaves", "Harvest Festivals", "Pumpkin Spice", "Equinox Science", "Cider"]),
    ("Week 37", "Oktoberfest", ["German Beer", "Bavaria", "Sausages", "Pretzels", "Polka Music"]),
    ("Week 38", "Coffee Day", ["Coffee Beans", "Starbucks Menu", "Caffeine Science", "Cafe Movies", "Mugs"]),
    ("Week 39", "Comic Con Season", ["Marvel vs DC", "Superheroes", "Cosplay", "Stan Lee cameos", "Graphic Novels"]),
    ("Week 40", "Columbus/Indigenous", ["Explorers", "Native Tribes", "New World", "Maps", "Sailing Terms"]),
    ("Week 41", "Spooky Season Begins", ["Classic Monsters", "Candy Corn", "Ghost Stories", "Witch Trials", "Vampire Lore"]),
    ("Week 42", "Horror Movies", ["Scream Queens", "Killer Villains", "Stephen King", "Zombie Survival", "Jump Scares"]),
    ("Week 43", "Halloween Prep", ["Costume Ideas", "Pumpkin Carving", "Haunted Houses", "Thriller Dance", "Candy Bars"]),
    ("Week 44", "Halloween", ["Trick or Treat", "Day of the Dead", "Orange & Black", "Famous Ghosts", "Scary Soundtracks"]),
    ("Week 45", "Election Day/Politics", ["Voting History", "Swing States", "Campaign Slogans", "White House", "Political Scandals"]),
    ("Week 46", "Veterans Day", ["Military Ranks", "War Movies", "Medal of Honor", "Peace Treaties", "Poppy Flowers"]),
    ("Week 47", "Thanksgiving Prep", ["Turkey Talk", "Side Dishes", "Pilgrims", "Mayflower", "Giving Thanks"]),
    ("Week 48", "Thanksgiving", ["Macy's Parade", "Football Tradition", "Black Friday origins", "Pie Varieties", "Leftovers"]),
    ("Week 49", "Winter Is Coming", ["Game of Thrones", "Snow Science", "Ski Resorts", "Winter Olympics", "Hot Cocoa"]),
    ("Week 50", "Hanukkah", ["Menorah", "Dreidel", "Latkes", "Jewish History", "Eight Nights"]),
    ("Week 51", "Christmas", ["Santa Claus", "Reindeer Names", "Holiday Movies", "Carols", "Gift Giving"]),
    ("Week 52", "New Year's Eve", ["Times Square", "Auld Lang Syne", "Champagne Regions", "Party Hats", "Countdown"])
]

import datetime

import datetime

# Visual Themes (CSS Variables)
VISUAL_THEMES = {
    # Classic Jeopardy Theme (Global Override)
    "default": {
        "--bg-image": "url('/static/bg/bg_jeopardy_set.png')",
        "--bg-color": "#000000",
        "--bg-overlay": "radial-gradient(circle at center, rgba(6, 12, 233, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%)", # Slight blue tint
        "--glass-bg": "rgba(6, 12, 233, 0.3)", # For panels
        "--border-color": "rgba(255, 255, 255, 0.1)",
        "--accent-color": "#FFCC00", # Gold
        "--text-color": "#FFFFFF",
        "--button-bg": "rgba(6, 12, 233, 0.8)",     # Blue but transparent
        "--button-shadow": "none"
    }
}

# Apply default classic theme to all keys for consistency
for key in ["winter", "valentine", "st_patrick", "summer", "halloween", "christmas", "patriotic", "spring", "autumn", "party", "cinema", "sports", "school", "money", "pub"]:
    VISUAL_THEMES[key] = VISUAL_THEMES["default"]

THEME_KEYWORDS = {
    "Valentine": "valentine",
    "Love": "valentine",
    "Patrick": "st_patrick", # Corrected to match VISUAL_THEMES key
    "Shamrock": "st_patrick", # Corrected to match VISUAL_THEMES key
    "Easter": "spring",
    "Spring": "spring",
    "Mother": "spring",
    "Flower": "spring",
    "Summer": "summer",
    "Sun": "summer",
    "Beach": "summer",
    "July": "summer",
    "Independence": "patriotic",
    "Memorial": "patriotic",
    "Patriot": "patriotic",
    "Veterans": "patriotic",
    "Labor": "patriotic",
    "Flag": "patriotic",
    "Halloween": "halloween",
    "Spooky": "halloween",
    "Horror": "halloween",
    "Witch": "halloween",
    "Thanksgiving": "autumn",
    "Turkey": "autumn",
    "Fall": "autumn",
    "Autumn": "autumn",
    "Coffee": "autumn",
    "Harvest": "autumn",
    "Christmas": "christmas",
    "Holiday": "christmas",
    "Santa": "christmas",
    "Winter": "winter",
    "Snow": "winter",
    "Cold": "winter",
    "Resolution": "party", # New Year
    "New Year": "party",
    "Party": "party",
    "Award": "cinema",
    "Oscar": "cinema",
    "Movie": "cinema",
    "Film": "cinema",
    "Super Bowl": "sports",
    "Football": "sports",
    "NFL": "sports",
    "Olympics": "sports",
    "Masters": "sports",
    "Golf": "sports",
    "Derby": "sports",
    "Sport": "sports",
    "School": "school",
    "Graduation": "school",
    "Class": "school",
    "Tax": "money",
    "Money": "money",
    "Finance": "money",
    "Beer": "pub",
    "Oktoberfest": "pub",
    "Pub": "pub"
}

def get_theme(title):
    t = title.lower()
    for keyword, theme_name in THEME_KEYWORDS.items():
        if keyword.lower() in t:
            return VISUAL_THEMES[theme_name]
    
    # Fallback for month-based themes if no keyword matches
    if "jan" in t: return VISUAL_THEMES["winter"]
    if "dec" in t: return VISUAL_THEMES["christmas"]
    
    return VISUAL_THEMES["default"]


from trivia_content import THEMED_CONTENT, GENERAL_POOL
import random

# ... (Previous imports and theme definitions are mapped or imported if distinct)
# To avoid duplications, I will stick to the logic:
# 1. Iterate THEMES
# 2. For each category in theme, look up in THEMED_CONTENT
# 3. If not found, pick a random category from GENERAL_POOL to replace it
# 4. For Round 2, use GENERAL_POOL exclusively

def generate_games():
    output_dir = "games"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find first Tuesday of 2026
    d = datetime.date(2026, 1, 1)
    while d.weekday() != 1: # 0=Mon, 1=Tue
        d += datetime.timedelta(days=1)
    
    general_cats_keys = list(GENERAL_POOL.keys())
    
    for week_num, (title_prefix, theme_name, cats) in enumerate(THEMES, 1):
        # Format date: "Jan 06"
        date_str = d.strftime("%b %d")
        full_title = f"{title_prefix} ({date_str}): {theme_name}"
        
        # Advance 7 days for next iteration
        d += datetime.timedelta(days=7)
        
        file_id = f"week_{week_num:02d}"
        
        # Get Theme
        theme_data = get_theme(full_title)

        game = {
            "title": full_title,
            "theme": theme_data,
            "round_1": {},
            "round_2": {},
            "final_jeopardy": {
                "category": "General Knowledge", # Fallback category
                "clue": "This chemical element, symbol Au, is the most malleable of all metals.",
                "answer": "Gold",
                "type": "text"
            }
        }
        
        # Improve FJ Logic: Pick a random '1000' value question from a random category
        # to serve as a 'Hard' Final Jeopardy if we don't have a specific theme one.
        fj_cat = random.choice(general_cats_keys)
        if THEMED_CONTENT.get(theme_name):
             # If we had a real theme, maybe we have a FJ for it? 
             # For now, just randomization is infinitely better than "Placeholder".
             pass
             
        fj_q = random.choice(GENERAL_POOL[fj_cat])
        game["final_jeopardy"]["category"] = fj_cat
        game["final_jeopardy"]["clue"] = fj_q["clue"]
        game["final_jeopardy"]["answer"] = fj_q["answer"]
        
        # Populate Round 1 (Themed)
        # We attempt to find the specific Category in our database.
        # If not found, we swap in a General Category to ensure PLAYABILITY.
        
        used_general = [] # Track what we used this week so we don't duplicate
        
        for cat in cats:
            # Check if we have specific content
            if cat in THEMED_CONTENT:
                game["round_1"][cat] = THEMED_CONTENT[cat]
            else:
                # Fallback: Pick a general category we haven't used yet
                # We try to pick one that isn't in Round 2 either
                candidates = [c for c in general_cats_keys if c not in used_general]
                if not candidates: candidates = general_cats_keys # recycle if desperation
                
                fallback_cat = random.choice(candidates)
                used_general.append(fallback_cat)
                
                # We use the General Content, but we might want to keep the "Theme Title" 
                # or just switch to the Fallback Title so it matches the questions?
                # Using "Gym Failures" title with "Science" questions is confusing.
                # BETTER: Switch the Category Name to the Fallback Name.
                
                game["round_1"][fallback_cat] = GENERAL_POOL[fallback_cat]

        # Populate Round 2 (General)
        # We need 5 general categories.
        r2_candidates = [c for c in general_cats_keys if c not in game["round_1"]]
        # Ensure we have enough
        while len(r2_candidates) < 5:
             r2_candidates.append(random.choice(general_cats_keys))

        # We need a stable subset for consistency or random? Random is fun.
        # But for 52 weeks, if we only have 10 General pools, it will get repetitive.
        # For this "MVP" fix, repetition of real questions is better than "Placeholders".
        
        selected_r2 = r2_candidates[:5]
        for cat in selected_r2:
            game["round_2"][cat] = GENERAL_POOL[cat]

        # Write to file
        with open(os.path.join(output_dir, f"{file_id}.json"), 'w') as f:
            json.dump(game, f, indent=4)
            
    print(f"Generated {len(THEMES)} games in {output_dir}/")

if __name__ == "__main__":
    generate_games()
