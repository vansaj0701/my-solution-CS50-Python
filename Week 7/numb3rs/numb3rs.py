import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_list = ip.split(".")
    for i in ip_list:
        if (len(ip_list) == 4) and (0 <= int(i) <= 255):
            continue
        else:
            return False

    return True


if __name__ == "__main__":
    main()
