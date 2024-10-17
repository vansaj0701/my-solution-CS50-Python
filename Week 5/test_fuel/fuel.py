def convert(fraction):
    sep = fraction.split("/")

    x, y = sep[0], sep[1]

    if y == '0':
        raise ZeroDivisionError

    elif x.isalpha() or y.isalpha():
        raise ValueError

    else:
        result = round((int(x) / int(y)) * 100)
        return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 100 >= percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"


def main():
    while True:
        try:
            fuel = input("Fraction: ")
            if convert(fuel):
                print(gauge(fuel))
                break
            else:
                continue
        except (ZeroDivisionError, ValueError):
            continue


if __name__ == "__main__":
    main()
