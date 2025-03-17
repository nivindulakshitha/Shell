import shutil
import sys
builtin_commands = {}

def command(func):
    builtin_commands[func.__name__.split("_")[1]] = func
    return func

@command
def shell_exit(args):
    exit(int(args[0]))

@command
def shell_echo(args):
    sys.stdout.write(" ".join(args) + "\n")

@command
def shell_type(args):
    if args[0] in builtin_commands:
        sys.stdout.write(f"{args[0]} is a shell builtin\n")
    elif path := shutil.which(args[0]):
        sys.stdout.write(f"{args[0]} is {path}\n")
    else:
        sys.stdout.write(f"{args[0]}: not found\n")

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        cmd, *args = command.split()
        if cmd in builtin_commands:
            builtin_commands[cmd](args)
        else:
            sys.stdout.write(f"{cmd}: command not found\n")

if __name__ == "__main__":
    main()