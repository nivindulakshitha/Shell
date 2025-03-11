import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        command, *args = command.split()

        match command:
            case "exit":
                break

            case "echo":
                sys.stdout.write(" ".join(args))
                
            case "type":
                if args[0] == "echo":  
                    sys.stdout.write("echo is a shell builtin\n")
                elif args[0] == "exit":
                    sys.stdout.write("exit is a shell builtin\n")
                else:
                    sys.stdout.write(f"{args[0]}: not found\n")

            case default:
                sys.stdout.write(f"{command}: command not found\n")
                
    return


if __name__ == "__main__":
    main()
