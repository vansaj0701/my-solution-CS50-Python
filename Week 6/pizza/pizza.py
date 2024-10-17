import sys
from tabulate import tabulate
import csv


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
    if file.endswith(".csv"):
        return True
    else:
        return False


def line_of_code(file):
    data_list = []
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            for data in reader:
                data_list.append(data)

            header = data_list[0]
            row = data_list[1:]

    except FileNotFoundError:
        sys.exit("File doesn't exists")

    return tabulate(row, header, tablefmt="grid")


main()
