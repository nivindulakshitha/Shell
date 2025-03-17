import sys
import os
def main():
    commands = {"exit", "echo", "type"}
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input().split()
        # if command[0] not in commands:
        #     print(f"${command[0]}: command not found")
        # elif command[0] == "exit" and command[1] == "0":
        #     sys.exit(0)
        # elif command[0] == "echo":
        #     print(" ".join(command[1:]))
        match command[0]:
            case "exit":
                if command[1] == "0":
                    sys.exit(0)
            case "echo":
                print(" ".join(command[1:]))
            case "type":
                if command[1] in commands:
                    print(f"{command[1]} is a shell builtin")
                else:
                    paths = os.getenv("PATH").split(":")
                    # print(paths)
                    for path in paths:
                        path_to_command = f"{path}/{command[1]}"
                        # print(path_to_command)
                        if os.path.exists(path_to_command):
                            print(f"{command[1]} is {path_to_command}")
                            break
                    else:
                        print(f"{command[1]}: not found")
            case "pwd":
                print(f"{os.getcwd()}")
            case _:
                if os.path.exists(command[0]):
                    os.system(" ".join(command))
                else:
                    # print("i'm here")
                    print(f"${command[0]}: command not found")
if __name__ == "__main__":
    main()