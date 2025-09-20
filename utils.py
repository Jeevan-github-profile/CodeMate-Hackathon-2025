history = []

def add_history(command):
    history.append(command)

def show_history():
    return "\n".join(f"{i+1}: {cmd}" for i, cmd in enumerate(history))

def handle_invalid(command):
    return f"Invalid command: {command}"
