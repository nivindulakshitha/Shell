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

            case default:
                print(f"{command}: command not found")
                
    return


if __name__ == "__main__":
    main()
