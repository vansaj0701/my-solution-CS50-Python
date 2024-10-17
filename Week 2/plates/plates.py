def vanity_plates(plate):
    char_count = 0
    if 2 <= len(plate) <= 6:
        for char in plate:
            if char.isalpha():
                char_count += 1
            else:
                break
        if char_count == 6:
            char_count -= 1

        if 6 > char_count >= 2 and plate[char_count] != "0":
            if plate[::].isalpha():
                return True

            elif plate[:char_count].isalpha():
                if plate[char_count:].isnumeric():
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

    if (vanity_plates(plate_number)):
        print("Valid")
    else:
        print("Invalid")


main()
