from datetime import datetime, date
import inflect
import sys

p = inflect.engine()


class Minutes:
    def __init__(self, dob, c_date):
        self.dob = dob
        self.c_date = c_date

    def convert(self):
        difference = self.c_date - self.dob
        minutes = (difference.days) * 24 * 60
        return round(int(minutes))

    def __str__(self):
        return f"{p.number_to_words(self.convert()).capitalize().replace("and ", "")} minutes"


def main():
    dob = input("Date of Birth: ").strip()
    current_date = date.today()

    try:
        date_object = datetime.strptime(dob, '%Y-%m-%d').date()
        print(f"{Minutes(date_object, current_date)}")
    except ValueError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
