import sys
import csv

data_list = []


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if (input_file(sys.argv[1])):
            output_file(sys.argv[2])
        else:
            sys.exit("Error")


def input_file(before):
    try:
        with open(before, "r") as file:
            reader = csv.DictReader(file)
            for data in reader:
                last, first = data['name'].split(", ")
                data_dict = {
                    'first name': first,
                    'last name': last,
                    'house': data['house']
                }

                data_list.append(data_dict)
    except FileNotFoundError:
        sys.exit("File does not exists")

    return data_list


def output_file(after):
    try:
        with open(after, "w") as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for data in data_list:
                writer.writerow({
                    'first': data['first name'],
                    'last': data['last name'],
                    'house': data['house'],
                })
    except FileNotFoundError:
        sys.exit("File does not exists")

    return True


main()
