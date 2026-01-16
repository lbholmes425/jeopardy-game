
GAMES = {
    "original": {
        "title": "Classic Trivia",
        "theme": {
            "--bg-image": "url('/static/bg/bg_default_1768430577284.png')",
            "--bg-overlay": "radial-gradient(circle at center, rgba(49, 46, 129, 0.4) 0%, rgba(2, 6, 23, 0.8) 100%)",
            "--glass-bg": "rgba(30, 41, 59, 0.7)",
            "--border-color": "rgba(255, 255, 255, 0.1)",
            "--accent-color": "#fbbf24", 
            "--text-color": "#f8fafc",
            "--button-bg": "linear-gradient(135deg, #4f46e5 0%, #3730a3 100%)",
            "--button-shadow": "0 4px 0 #1e1b4b"
        },
        "round_1": {
            "Literature": [
                {"value": 100, "clue": "This Dr. Seuss character famously insists he does not like green eggs and ham.", "answer": "Who is Sam-I-Am?", "type": "text"},
                {"value": 200, "clue": "This Hogwarts house values bravery, nerve, and chivalry.", "answer": "What is Gryffindor?", "type": "text"},
                {"value": 300, "clue": "In Charlotte’s Web, this is the name of the pig Charlotte saves.", "answer": "Who is Wilbur?", "type": "text"},
                {"value": 400, "clue": "This classic novel opens with the line, “Call me Ishmael.”", "answer": "What is Moby-Dick?", "type": "text"},
                {"value": 500, "clue": "In George Orwell’s 1984, this phrase represents the government’s control over truth and history.", "answer": "What is “Big Brother is watching you”?", "type": "text"},
            ],
            "Sports": [
                {"value": 100, "clue": "This SEC stadium is nicknamed “Death Valley.”", "answer": "What is Tiger Stadium (LSU)?", "type": "text"},
                {"value": 200, "clue": "He won the 1985 Heisman Trophy while playing at Auburn University.", "answer": "Who is Bo Jackson?", "type": "text"},
                {"value": 300, "clue": "This MLB player hit 61 home runs in 1961, breaking Babe Ruth’s record.", "answer": "Who is Roger Maris?", "type": "text"},
                {"value": 400, "clue": "This tennis star completed the Open Era Grand Slam in 1969.", "answer": "Who is Rod Laver?", "type": "text"},
                {"value": 500, "clue": "This NBA team drafted Kobe Bryant but traded him before he ever played.", "answer": "Who are the Charlotte Hornets?", "type": "text"},
            ],
            "Music": [
                {"value": 100, "clue": "This artist sang Purple Rain and played nearly every instrument on the album.", "answer": "Who is Prince?", "type": "text"},
                {"value": 200, "clue": "This band released Rumours in 1977.", "answer": "Who are Fleetwood Mac?", "type": "text"},
                {"value": 300, "clue": "This Michael Jackson album is the best-selling album in history.", "answer": "What is Thriller?", "type": "text"},
                {"value": 400, "clue": "This guitarist is nicknamed Slowhand.", "answer": "Who is Eric Clapton?", "type": "text"},
                {"value": 500, "clue": "This band played their final show on the Apple rooftop in 1969.", "answer": "Who are The Beatles?", "type": "text"},
            ],
            "Animals": [
                {"value": 100, "clue": "This is the fastest land animal.", "answer": "What is the cheetah?", "type": "text"},
                {"value": 200, "clue": "This animal has the largest brain.", "answer": "What is the sperm whale?", "type": "text"},
                {"value": 300, "clue": "A group of these animals is called a parliament.", "answer": "What is an owl?", "type": "text"},
                {"value": 400, "clue": "This animal can sleep standing up.", "answer": "What is a horse?", "type": "text"},
                {"value": 500, "clue": "This bear species eats mostly bamboo.", "answer": "What is the giant panda?", "type": "text"},
            ],
            "Movies": [
                {"value": 100, "clue": "This movie follows a man in a fake reality TV world.", "answer": "What is The Truman Show?", "type": "text"},
                {"value": 200, "clue": "Who said Hold onto your butts in Jurassic Park.", "answer": "Who is Ray Arnold?", "type": "text"},
                {"value": 300, "clue": "Identify this movie from the image.", "answer": "What is Pulp Fiction?", "type": "image", "url": "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg"}, 
                {"value": 400, "clue": "This courtroom drama takes place in one room.", "answer": "What is 12 Angry Men?", "type": "text"},
                {"value": 500, "clue": "Guest Reader: Who is this actor?", "answer": "Who is Kurt Russell?", "type": "video", "url": "https://www.w3schools.com/html/mov_bbb.mp4"},
            ],
        },
        "round_2": {
            "World History": [
                {"value": 200, "clue": "This wall fell in 1989.", "answer": "What is the Berlin Wall?", "type": "text"},
                {"value": 400, "clue": "First emperor of unified China.", "answer": "Who is Qin Shi Huang?", "type": "text"},
                {"value": 600, "clue": "This ship sank in 1912.", "answer": "What is the Titanic?", "type": "text"},
                {"value": 800, "clue": "This treaty ended World War I.", "answer": "What is the Treaty of Versailles?", "type": "text"},
                {"value": 1000, "clue": "This ancient wonder stood in Alexandria.", "answer": "What is the Lighthouse of Alexandria?", "type": "text"},
            ],
            "Quotes": [
                {"value": 200, "clue": "Speak softly and carry a big stick.", "answer": "Who is Theodore Roosevelt?", "type": "text"},
                {"value": 400, "clue": "I think, therefore I am.", "answer": "Who is René Descartes?", "type": "text"},
                {"value": 600, "clue": "One small step for man.", "answer": "Who is Neil Armstrong?", "type": "text"},
                {"value": 800, "clue": "Give me liberty or give me death.", "answer": "Who is Patrick Henry?", "type": "text"},
                {"value": 1000, "clue": "To be or not to be.", "answer": "Who is William Shakespeare?", "type": "text"},
            ],
            "Science": [
                {"value": 200, "clue": "Hottest planet.", "answer": "What is Venus?", "type": "text"},
                {"value": 400, "clue": "Chemical symbol Fe.", "answer": "What is iron?", "type": "text"},
                {"value": 600, "clue": "Powerhouse of the cell.", "answer": "What are mitochondria?", "type": "text"},
                {"value": 800, "clue": "Galaxy colliding with Milky Way.", "answer": "What is Andromeda?", "type": "text"},
                {"value": 1000, "clue": "Smallest unit of matter.", "answer": "What is an atom?", "type": "text"},
            ],
            "TV Shows": [
                {"value": 200, "clue": "Ross, Rachel, Monica, Chandler, Joey, Phoebe.", "answer": "What is Friends?", "type": "text"},
                {"value": 400, "clue": "Walter White show.", "answer": "What is Breaking Bad?", "type": "text"},
                {"value": 600, "clue": "Based on George R. R. Martin novels.", "answer": "What is Game of Thrones?", "type": "text"},
                {"value": 800, "clue": "Long running animated Springfield show.", "answer": "What is The Simpsons?", "type": "text"},
                {"value": 1000, "clue": "Mockumentary office comedy.", "answer": "What is The Office?", "type": "text"},
            ],
            "Food & Drink": [
                {"value": 200, "clue": "Layered pasta dish.", "answer": "What is lasagna?", "type": "text"},
                {"value": 400, "clue": "Country that invented croissants.", "answer": "What is France?", "type": "text"},
                {"value": 600, "clue": "Yellow curry spice.", "answer": "What is turmeric?", "type": "text"},
                {"value": 800, "clue": "Vodka ginger beer lime cocktail.", "answer": "What is a Moscow Mule?", "type": "text"},
                {"value": 1000, "clue": "Raw fish over rice.", "answer": "What is sushi?", "type": "text"},
            ],
        },
        "final_jeopardy": {
            "category": "Hidden Connections",
            "clue": "TMNT leader, the Boy Who Lived, and the Millionaire host share this first name.",
            "answer": "Who is Michael?",
            "type": "text"
        }
    },

    "pub_culture": {
        "title": "Pub Culture",
        "theme": {
            "--bg-image": "url('/static/bg/bg_stpatrick_1768430615527.png')",
            "--bg-overlay": "radial-gradient(circle at center, rgba(6, 78, 59, 0.4) 0%, rgba(2, 44, 34, 0.9) 100%)",
             "--glass-bg": "rgba(6, 78, 59, 0.7)",
            "--border-color": "rgba(167, 243, 208, 0.2)",
            "--accent-color": "#fbbf24",
            "--text-color": "#ecfdf5",
            "--button-bg": "linear-gradient(135deg, #059669 0%, #065f46 100%)",
            "--button-shadow": "0 4px 0 #064e3b"
        },
        "round_1": {
            "Cocktails": [
                {"value": 100, "clue": "Vodka and Orange Juice.", "answer": "What is a Screwdriver?", "type": "text"},
                {"value": 200, "clue": "Gin and Vermouth, shaken not stirred.", "answer": "What is a Martini?", "type": "text"},
                {"value": 300, "clue": "Tequila, Triple Sec, Lime Juice.", "answer": "What is a Margarita?", "type": "text"},
                {"value": 400, "clue": "Whiskey, Sugar, Bitters, Orange Peel.", "answer": "What is an Old Fashioned?", "type": "text"},
                {"value": 500, "clue": "Rum, Mint, Lime, Soda, Sugar.", "answer": "What is a Mojito?", "type": "text"},
            ],
            "Bar Songs": [
                {"value": 100, "clue": "Just a small town girl, living in a lonely world.", "answer": "What is Don't Stop Believin'?", "type": "text"},
                {"value": 200, "clue": "Country roads, take me home.", "answer": "What is Take Me Home, Country Roads?", "type": "text"},
                {"value": 300, "clue": "Caroline! Bum Bum Bum!", "answer": "What is Sweet Caroline?", "type": "text"},
                {"value": 400, "clue": "I would walk 500 miles.", "answer": "What is I'm Gonna Be (500 Miles)?", "type": "text"},
                {"value": 500, "clue": "Closing time, open all the doors...", "answer": "What is Closing Time?", "type": "text"},
            ],
             "Beer Brands": [
                {"value": 100, "clue": "The King of Beers.", "answer": "What is Budweiser?", "type": "text"},
                {"value": 200, "clue": "It's Miller Time.", "answer": "What is Miller High Life (or Miller Lite)?", "type": "text"},
                {"value": 300, "clue": "Mexican beer often served with a lime.", "answer": "What is Corona?", "type": "text"},
                {"value": 400, "clue": "Irish dry stout.", "answer": "What is Guinness?", "type": "text"},
                {"value": 500, "clue": "Identify this logo.", "answer": "What is Heineken?", "type": "image", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Heineken_logo.svg/2560px-Heineken_logo.svg.png"},
            ],
            "Party Fouls": [
                {"value": 100, "clue": "Spilling a full drink.", "answer": "What is Party Foul?", "type": "text"},
                {"value": 200, "clue": "Leaving without paying.", "answer": "What is Dine and Dash?", "type": "text"},
                {"value": 300, "clue": "Double dipping a chip.", "answer": "What is gross?", "type": "text"},
                {"value": 400, "clue": "Talking politics at the bar.", "answer": "What is a buzzkill?", "type": "text"},
                {"value": 500, "clue": "Ordering a complicated drink during rush.", "answer": "What is annoying the bartender?", "type": "text"},
            ],
             "Hangover Cures": [
                {"value": 100, "clue": "Drinking water.", "answer": "What is Hydration?", "type": "text"},
                {"value": 200, "clue": "Hair of the dog.", "answer": "What is drinking more alcohol?", "type": "text"},
                {"value": 300, "clue": "Greasy breakfast food.", "answer": "What is Waffle House?", "type": "text"},
                {"value": 400, "clue": "Pain relievers (Advil/Tylenol).", "answer": "What is Ibuprofen/Acetaminophen?", "type": "text"},
                {"value": 500, "clue": "Prairie Oyster ingredients.", "answer": "What is raw egg, worcestershire, hot sauce?", "type": "text"},
            ],
        },
        "round_2": {
             "Sports Bars": [
                {"value": 200, "clue": "Main event on Sundays.", "answer": "What is NFL Football?", "type": "text"},
                {"value": 400, "clue": "March Madness sport.", "answer": "What is College Basketball?", "type": "text"},
                {"value": 600, "clue": "Sport with 9 innings.", "answer": "What is Baseball?", "type": "text"},
                {"value": 800, "clue": "Puck and stick.", "answer": "What is Hockey?", "type": "text"},
                {"value": 1000, "clue": "The Beautiful Game.", "answer": "What is Soccer (Football)?", "type": "text"},
            ],
             "Famous Bars": [
                {"value": 200, "clue": "Where everybody knows your name.", "answer": "What is Cheers?", "type": "text"},
                {"value": 400, "clue": "Moe's Tavern is in this town.", "answer": "What is Springfield?", "type": "text"},
                {"value": 600, "clue": "The pub in Shaun of the Dead.", "answer": "What is The Winchester?", "type": "text"},
                {"value": 800, "clue": "Star Wars cantina planet.", "answer": "What is Tatooine?", "type": "text"},
                {"value": 1000, "clue": "It's Always Sunny bar.", "answer": "What is Paddy's Pub?", "type": "text"},
            ],
             "Pub Trivia": [
                {"value": 200, "clue": "Capital of France.", "answer": "What is Paris?", "type": "text"},
                {"value": 400, "clue": "Largest Ocean.", "answer": "What is the Pacific?", "type": "text"},
                {"value": 600, "clue": "Currency of UK.", "answer": "What is the Pound Sterling?", "type": "text"},
                {"value": 800, "clue": "Number of hearts an octopus has.", "answer": "What is Three?", "type": "text"},
                {"value": 1000, "clue": "Speed of light.", "answer": "What is 299,792,458 m/s (or very fast)?", "type": "text"},
            ],
              "Darts & Pool": [
                {"value": 200, "clue": "Center of the dart board.", "answer": "What is the Bullseye?", "type": "text"},
                {"value": 400, "clue": "Black ball in pool.", "answer": "What is the 8-ball?", "type": "text"},
                {"value": 600, "clue": "Distance to throw darts.", "answer": "What is 7 feet 9.25 inches?", "type": "text"},
                {"value": 800, "clue": "Perfect score in bowling (bar game adjacent).", "answer": "What is 300?", "type": "text"},
                {"value": 1000, "clue": "Cue ball color.", "answer": "What is White?", "type": "text"},
            ],
            "Bar Food": [
                {"value": 200, "clue": "Spicy chicken wings city.", "answer": "What is Buffalo?", "type": "text"},
                {"value": 400, "clue": "Salted twisted dough.", "answer": "What is a Pretzel?", "type": "text"},
                {"value": 600, "clue": "Tortilla chips with cheese.", "answer": "What are Nachos?", "type": "text"},
                {"value": 800, "clue": "Deep fried cheese stick.", "answer": "What is Mozzarella Stick?", "type": "text"},
                {"value": 1000, "clue": "Pickled egg origin.", "answer": "What is traditional British pub food?", "type": "text"},
            ],
        },
        "final_jeopardy": {
            "category": "Toast",
            "clue": "This Yiddish toast means 'To Life'.",
            "answer": "What is L'Chaim?",
            "type": "text"
        }
    },
    
    "90s_nostalgia": {
        "title": "90s Nostalgia",
        "theme": {
            "--bg-image": "url('/static/bg/bg_summer_1768430634784.png')",
            "--bg-overlay": "radial-gradient(circle at center, rgba(236, 72, 153, 0.4) 0%, rgba(80, 7, 36, 0.9) 100%)",
            "--glass-bg": "rgba(255, 255, 255, 0.1)",
            "--border-color": "rgba(255, 0, 255, 0.5)",
            "--accent-color": "#00ff00",
            "--text-color": "#ffffff",
            "--button-bg": "linear-gradient(135deg, #ec4899 0%, #db2777 100%)",
            "--button-shadow": "0 4px 0 #831843"
        },
        "round_1": {
            "Cartoons": [
                {"value": 100, "clue": "Football head.", "answer": "Who is Hey Arnold?", "type": "text"},
                {"value": 200, "clue": "Babies exploring the world.", "answer": "What is Rugrats?", "type": "text"},
                {"value": 300, "clue": "Cat and Dog attached.", "answer": "What is CatDog?", "type": "text"},
                {"value": 400, "clue": "Scientist boy with a lab.", "answer": "What is Dexter's Laboratory?", "type": "text"},
                {"value": 500, "clue": "Three girls with superpowers.", "answer": "What is Powerpuff Girls?", "type": "text"},
            ],
            "Music": [
                {"value": 100, "clue": "Smells Like Teen Spirit band.", "answer": "Who is Nirvana?", "type": "text"},
                {"value": 200, "clue": "Baby One More Time.", "answer": "Who is Britney Spears?", "type": "text"},
                {"value": 300, "clue": "I Want It That Way.", "answer": "Who are the Backstreet Boys?", "type": "text"},
                {"value": 400, "clue": "Wannabe.", "answer": "Who are the Spice Girls?", "type": "text"},
                {"value": 500, "clue": "Creep.", "answer": "Who are Radiohead (or TLC)?", "type": "text"},
            ],
            "Movies": [
                {"value": 100, "clue": "King of the World.", "answer": "What is Titanic?", "type": "text"},
                {"value": 200, "clue": "Dinosaurs park.", "answer": "What is Jurassic Park?", "type": "text"},
                {"value": 300, "clue": "First rule is don't talk about it.", "answer": "What is Fight Club?", "type": "text"},
                {"value": 400, "clue": "I see dead people.", "answer": "What is The Sixth Sense?", "type": "text"},
                {"value": 500, "clue": "Keanu Reeves stops a bullet.", "answer": "What is The Matrix?", "type": "text"},
            ],
            "Tech": [
                {"value": 100, "clue": "Dial-up sound.", "answer": "What is the Internet?", "type": "text"},
                {"value": 200, "clue": "Virtual pet on a keychain.", "answer": "What is Tamagotchi?", "type": "text"},
                {"value": 300, "clue": "Portable CD player.", "answer": "What is Discman?", "type": "text"},
                {"value": 400, "clue": "File sharing service sued by Metallica.", "answer": "What is Napster?", "type": "text"},
                {"value": 500, "clue": "Search engine before Google.", "answer": "What is AltaVista/Yahoo/AskJeeves?", "type": "text"},
            ],
            "Toys": [
                {"value": 100, "clue": "Tickle Me...", "answer": "Who is Elmo?", "type": "text"},
                {"value": 200, "clue": "Stuffed animals with tags.", "answer": "What are Beanie Babies?", "type": "text"},
                {"value": 300, "clue": "Pog game pieces.", "answer": "What are Pogs?", "type": "text"},
                {"value": 400, "clue": "Talking owl/bird robot.", "answer": "What is Furby?", "type": "text"},
                {"value": 500, "clue": "Action figure that stretches.", "answer": "Who is Armstrong?", "type": "text"},
            ],
        },
        "round_2": {
             "TV Shows": [
                {"value": 200, "clue": "Show about nothing.", "answer": "What is Seinfeld?", "type": "text"},
                {"value": 400, "clue": "Will Smith lives in Bel-Air.", "answer": "What is Fresh Prince?", "type": "text"},
                {"value": 600, "clue": "The Truth is Out There.", "answer": "What is X-Files?", "type": "text"},
                {"value": 800, "clue": "Vampire Slayer.", "answer": "Who is Buffy?", "type": "text"},
                {"value": 1000, "clue": "Twin Peaks creator.", "answer": "Who is David Lynch?", "type": "text"},
            ],
             "Fashion": [
                {"value": 200, "clue": "Baggy pants.", "answer": "What are JNCOs?", "type": "text"},
                {"value": 400, "clue": "Flannel shirts style.", "answer": "What is Grunge?", "type": "text"},
                {"value": 600, "clue": "Slap on wrist accessory.", "answer": "What are Slap Bracelets?", "type": "text"},
                {"value": 800, "clue": "Shoes with lights.", "answer": "What are Light-up Sneakers (LA Gear)?", "type": "text"},
                {"value": 1000, "clue": "Hair accessory for ponytails.", "answer": "What is a Scrunchie?", "type": "text"},
            ],
            "Slang": [
                {"value": 200, "clue": "Good thing.", "answer": "What is Phat / Dope / Fly?", "type": "text"},
                {"value": 400, "clue": "As if!", "answer": "What is Clueless quote?", "type": "text"},
                {"value": 600, "clue": "Talk to the hand.", "answer": "What is dismissive?", "type": "text"},
                {"value": 800, "clue": "Booyah!", "answer": "What is excitement?", "type": "text"},
                {"value": 1000, "clue": "Getting Jiggy with it.", "answer": "What is dancing?", "type": "text"},
            ],
             "Events": [
                {"value": 200, "clue": "Y2K fear.", "answer": "What is Millennium Bug?", "type": "text"},
                {"value": 400, "clue": "O.J. Simpson vehicle.", "answer": "What is White Ford Bronco?", "type": "text"},
                {"value": 600, "clue": "President impeached.", "answer": "Who is Bill Clinton?", "type": "text"},
                {"value": 800, "clue": "Dolly the Sheep.", "answer": "What is Cloning?", "type": "text"},
                {"value": 1000, "clue": "Princess Diana accident year.", "answer": "What is 1997?", "type": "text"},
            ],
            "Snacks": [
                {"value": 200, "clue": "Fruit Roll-Ups mostly.", "answer": "What is Fruit by the Foot?", "type": "text"},
                {"value": 400, "clue": "Dunkaroos dip.", "answer": "What is Frosting?", "type": "text"},
                {"value": 600, "clue": "Clear soda from Pepsi.", "answer": "What is Crystal Pepsi?", "type": "text"},
                {"value": 800, "clue": "Surge soda color.", "answer": "What is Green?", "type": "text"},
                {"value": 1000, "clue": "3D Doritos shape.", "answer": "What is Triangle puff?", "type": "text"},
            ],
        },
        "final_jeopardy": {
            "category": "90s endings",
            "clue": "This sitcom ended in 1998 with the main characters in a jail cell.",
            "answer": "What is Seinfeld?",
            "type": "text"
        }
    }
}
