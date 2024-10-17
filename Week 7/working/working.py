import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d*):?(\d*)? (AM|PM) to (\d*):?(\d*) (AM|PM)"

    match = re.search(pattern, s)

    if match:
        if match.group(2).isnumeric():
            if int(match.group(2)) >= 60 and int(match.group(5)) >= 60:
                raise ValueError

        if match.group(3) == 'PM':
            convert_ante = int(match.group(1))+12
            convert_post = int(match.group(4))
        elif match.group(1) == '12' and match.group(4) == '12':
            convert_ante = 0
            convert_post = 12
        elif match.group(6) == 'PM':
            convert_post = int(match.group(4))+12
            convert_ante = int(match.group(1))
    else:
        raise ValueError

    return (f"{convert_ante:02}:00 to {convert_post:02}:00")


if __name__ == "__main__":
    main()
