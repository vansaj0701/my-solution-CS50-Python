from twttr import shorten


def test_twttr():
    assert shorten("this is cs50") == "ths s cs50"
    assert shorten("THIS IS CS50") == "THS S CS50"
    assert shorten("this is cs50.") == "ths s cs50."


def main():
    test_twttr()


if __name__ == "__main__":
    main()
