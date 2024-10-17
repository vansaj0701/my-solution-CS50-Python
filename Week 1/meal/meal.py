def main():
    time = input("What time is it? ")
    meal_time = convert(time)
    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")

    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")

    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")

    else:
        print()


def convert(time):
    str_hours, minutes = time.split(":")

    hours = int(str_hours)

    converted_time = float(hours) + float(minutes)/60
    return converted_time


if __name__ == "__main__":
    main()
