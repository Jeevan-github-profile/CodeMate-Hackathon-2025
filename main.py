import commands
import system_monitor
import utils
import codemate_ai

COMMANDS = {
    "ls": commands.ls,
    "pwd": commands.pwd,
    "cd": commands.cd,
    "mkdir": commands.mkdir,
    "rm": commands.rm,
    "cpu": lambda args: system_monitor.cpu_usage(),
    "mem": lambda args: system_monitor.memory_usage(),
    "ps": lambda args: system_monitor.processes(),
    "history": lambda args: utils.show_history(),
    "report": lambda args: codemate_ai.build_report()
}

def main():
    print("Welcome to Python Terminal Emulator (CodeMate Edition). Type 'exit' to quit.")
    while True:
        try:
            raw_input = input(">>> ").strip()
            if not raw_input:
                continue
            if raw_input == "exit":
                break

            parts = raw_input.split()
            cmd, args = parts[0], parts[1:]

            utils.add_history(raw_input)

            if cmd in COMMANDS:
                output = COMMANDS[cmd](args)
                if output:
                    print(output)
            else:
                print(utils.handle_invalid(cmd))
                suggestion = codemate_ai.mandatory_ai_check(cmd)
                if suggestion:
                    print("[CodeMate AI] " + suggestion)

        except KeyboardInterrupt:
            print("\nExiting terminal...")
            break

if __name__ == "__main__":
    main()
