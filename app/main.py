import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        command, *args = command.split()

        match command:
            case "exit 0":
                sys.exit(0)
                break

            case "echo":
                print(" ".join(args))

            case _:
                print(f"Command not found: {command}")
                
    return 0


if __name__ == "__main__":
    main()
