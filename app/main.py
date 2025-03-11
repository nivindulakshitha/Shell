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
                print(" ".join(args))

            case default:
                sys.stdout.write(f"{command}: command not found\n")
                
    return


if __name__ == "__main__":
    main()
