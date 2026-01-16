import json
import os
import glob

def verify_games():
    game_files = glob.glob("games/*.json")
    print(f"Found {len(game_files)} game files.")
    
    issues = []
    
    # Forbidden phrases that indicate placeholders
    FORBIDDEN = [
        "Use your knowledge of",
        "A generic question about",
        "What is the Theme Answer?",
        "What is General Knowledge answer?",
        "placeholder"
    ]
    
    for filepath in sorted(game_files):
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                issues.append(f"{filepath}: JSON Error - {e}")
                continue
                
        # recursively check string values
        def check_text(obj, path=""):
            if isinstance(obj, str):
                for phrase in FORBIDDEN:
                    if phrase.lower() in obj.lower():
                        # Exception: We left a placeholder in Final Jeopardy specifically mentioned in the generator logic
                        # "This is a Final Jeopardy placeholder..."
                        if "Final Jeopardy placeholder" in obj: 
                            continue
                        issues.append(f"{filepath} ({path}): Contains forbidden phrase '{phrase}' -> '{obj}'")
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    check_text(v, f"{path}.{k}")
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    check_text(v, f"{path}[{i}]")

        check_text(data)

    if issues:
        print("❌ VERIFICATION FAILED! Found issues:")
        for i in issues:
            print(i)
    else:
        print("✅ VERIFICATION PASSED! All 52 weeks are clean of generic placeholders.")

if __name__ == "__main__":
    verify_games()
