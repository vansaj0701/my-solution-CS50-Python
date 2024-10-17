import re


def main():
    print(parse(input("HTML: ")))


def parse(embedded):
    pattern = r'(.+)https?://(www\.)?youtube\.com/embed/(\w*)(.+)'
    match = re.search(pattern, embedded)

    if match:
        return (f"https://youtu.be/{match.group(3)}")


if __name__ == "__main__":
    main()
