import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if check_file(sys.argv[1]):
            print(f"{line_of_code(sys.argv[1])}")
        else:
            sys.exit("Not a Python file")


def check_file(file):
    if file.endswith(".py"):
        return True
    else:
        return False


def line_of_code(file):
    line_number = 0
    try:
        with open(file, "r") as f:
            reader = f.readlines()
            for line in reader:
                if line.lstrip().startswith("#") or line.strip() == "":
                    continue
                else:
                    line_number += 1
    except FileNotFoundError:
        return "File doesn't exists"

    return line_number


main()
