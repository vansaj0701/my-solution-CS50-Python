def fuel_gauge(fuel):
    sep = fuel.split("/")

    try:
        x, y = int(sep[0]), int(sep[1])

        try:
            result = round((x / y) * 100)
            if result <= 1:
                return "E"
            elif 100 >= result >= 99:
                return "F"
            elif x > y:
                return False
            else:
                return str(result)+"%"
        except ZeroDivisionError:
            return False

    except ValueError:
        return False


def main():
    while True:
        fuel = input("Fraction: ")
        if fuel_gauge(fuel):
            print(fuel_gauge(fuel))
            break
        else:
            continue


main()
