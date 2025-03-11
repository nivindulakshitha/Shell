import sys


def main():
    sys.stdout.write("$ ")
    command = input()

    if command == "exit 0":
        sys.exit(0)

    print(f"{command}: command not found")

    main()


if __name__ == "__main__":
    main()
