def is_valid(s):
    char_count = 0
    if 2 <= len(s) <= 6:
        for char in s:
            if char.isalpha():
                char_count += 1
            else:
                break
        if char_count == 6:
            char_count -= 1

        if 6 > char_count >= 2 and s[char_count] != "0":
            if s[::].isalpha():
                return True

            elif s[:char_count].isalpha():
                if s[char_count:].isnumeric():
                    return True
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False


def main():
    plate_number = input("Plate: ").strip()

    if (is_valid(plate_number)):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
