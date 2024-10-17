def main():
    print(count(input("Text: ")))


def count(s):
    #s = s.lower()
    um_count = 0
    word_list = s.split(" ")

    for um in word_list:
        if um.lower().startswith("um") and not um.lower().startswith("umm"):
            um_count += 1
        else:
            continue

    return um_count


if __name__ == "__main__":
    main()
