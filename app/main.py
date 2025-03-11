import sys


def main():
    sys.stdout.write("$ ")
    command = input()
    print(f"{command}: command not found")

    main()


if __name__ == "__main__":
    main()
