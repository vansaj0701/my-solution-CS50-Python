from datetime import datetime

formats = ["%d/%B/%Y", "%m/%d/%Y", "%B %d, %Y"]
date_format = ''
new_format = "%Y-%m-%d"


def main():
    while True:
        try:
            date = input("Date: ").strip()
            if (check_format(date)):
                print(f"{format_date(date, date_format)}")
                break
            else:
                continue
        except EOFError:
            break


def check_format(date):
    global date_format
    for i in formats:
        try:
            datetime.strptime(date, i)
            date_format += i
            return True
        except ValueError:
            continue


def format_date(date, format):
    date_object = datetime.strptime(date, format).date()
    new_date_format = date_object.strftime(new_format)
    return date_object


main()
