import sys
import os
PATH_SEP = os.pathsep
PATH = os.environ["PATH"]
BUILTINS = {"exit": "builtin", "type": "builtin", "echo": "builtin"}
def parse_path(path):
    path = path.split(PATH_SEP)
    path = [current_path for current_path in path if current_path]
    for current_path in path:
        if os.path.exists(current_path):
            files = (
                file
                for file in os.listdir(current_path)
                if os.path.isfile(os.path.join(current_path, file))
            )
        for file in files:
            if file not in BUILTINS:
                BUILTINS[file] = os.path.join(current_path, file)
def main():
    parse_path(PATH)
    while True:
        sys.stdout.write("$ ")
        args = input().split(" ")
        if len(args) == 0:
            continue
        else:
            command, *params = args
            if command == "exit":
                return 0
            elif command == "echo":
                print(*params)
            elif command == "type":
                arg_command = params[0]
                if arg_command in BUILTINS:
                    if BUILTINS[arg_command] == "builtin":
                        print(f"{arg_command} is a shell builtin")
                    else:
                        print(f"{arg_command} is {BUILTINS[arg_command]}")
                else:
                    print(f"{arg_command}: not found")
            elif command in BUILTINS:
                os.system(f"{command} {' '.join(params)}")
            else:
                print(f"{command}: command not found")
if __name__ == "__main__":
    main()