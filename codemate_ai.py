from utils import history

def build_report():
    return f"[CodeMate Build] Commands executed:\n" + "\n".join(history)

def mandatory_ai_check(command):
    # Very simple "AI" – suggest correction if typo
    suggestions = {
        "sl": "Did you mean 'ls'?",
        "pdw": "Did you mean 'pwd'?",
        "cd..": "Did you mean 'cd ..'?"
    }
    return suggestions.get(command, "")
