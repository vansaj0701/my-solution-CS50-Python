import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()


def main():
     if check_arg():
        text = input("Input: ").strip()
        if len(sys.argv) == 1:
            print(f"Output: {random_font(text)}")

        elif len(sys.argv) == 3:
            print(f"Output: {given_fonts(text)}")

        else:
            print("Invalid")


def check_arg():
    first_arg_list = ['--f', '--font', '-f', '-font']
    L = sys.argv
    if L[1] not in first_arg_list:
        sys.exit("Wrong argument")

    elif L[2] not in font_list:
        sys.exit("Wrong font")

    else:
        return True


def random_font(text):
    random_font = choice(font_list)
    figlet.setFont(font=random_font)
    random_styled_text = figlet.renderText(text)
    return random_styled_text


def given_fonts(text):
    figlet.setFont(font=sys.argv[2])
    given_styled_text = figlet.renderText(text)
    return given_styled_text


main()
