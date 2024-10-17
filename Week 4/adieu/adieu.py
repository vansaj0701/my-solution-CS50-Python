import inflect
p = inflect.engine()
name_list = []


def main():
    while True:
        try:
            text = input("Name: ").strip()
            if text != "":
                name_list.append(text)
            else:
                continue
        except EOFError:
            print(adieu(name_list))
            break


def adieu(name_list):
    natural_language = p.join(name_list)
    return "Adieu, adieu, to " + natural_language


main()
