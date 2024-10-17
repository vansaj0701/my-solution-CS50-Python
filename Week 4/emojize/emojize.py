import emoji

combine = []


def main():
    while True:
        try:
            alias = input("Input: ").strip()
            if find_alias(alias):
                print(f"Output: {emojized(combine)}")
                break
            else:
                continue
        except EOFError:
            break


def find_alias(word):
    for i in range(len(word)):
        if word[i] == ":":
            get_alias = word[i:]
            extra_words = word[:i]
            combine.append(get_alias)
            combine.append(extra_words)
            return combine
        else:
            continue


def emojized(combine):
    result = combine[-1] + combine[0]
    return emoji.emojize(result, language='alias')


main()
