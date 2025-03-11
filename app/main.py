import sys


def main():
    while True:
        print("$ ")
        command = input()

        command, *args = command.split()

        match command:
            case "exit":
                break

            case "echo":
                print(" ".join(args))
                
            case "type":
                if args[0] == "echo":  
                    print("echo is a shell builtin\n")
                elif args[0] == "exit":
                    print("exit is a shell builtin\n")
                else:
                    print(f"{args[0]}: not found\n")

            case default:
                print(f"{command}: command not found\n")
                
    return


if __name__ == "__main__":
    main()
