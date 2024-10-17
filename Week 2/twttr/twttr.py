def twittr(text):
    for char in text:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            text = text.replace(char, "")

    return text


def main():
    msg = input("Input: ").strip()

    print(f"Outout: {twittr(msg)}")


# FUNCTION CALL
main()
