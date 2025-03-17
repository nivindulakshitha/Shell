import sys
def main():
    while 1:
        sys.stdout.write("$ ")
        command = input()
        match command:
            case command if command.startswith("echo "):
                sys.stdout.write(f"{command[len("echo ") :]}\n")
            case "exit 0":
                return 0
            case command if command.startswith("type invalid"):
                sys.stdout.write(f"{command[len('type ') :]}: not found\n")
            case command if command.startswith("type "):
                sys.stdout.write(f"{command[len('type ') :]} is a shell builtin\n")
            case _:
                sys.stdout.write(f"{command}: command not found\n")
if __name__ == "__main__":
    main()