import requests
import random
import cowsay
from art import text2art


ascii_art = text2art("THE END", font="bubble")
the_end = "\n".join([f"\t\t\t\t{line}" for line in ascii_art.split("\n")])


def main():
    while True:
        print("-"*96)
        print(text2art("POETRY   EXPLORER", font="doom"))
        print(f"{"-"*45} MENU {"-"*45}")
        print("\t\t1. Random 25 Authors\t\t\t\t5. Poem by Line Count")
        print("\t\t2. Random 25 Titles\t\t\t\t6. Poem by Author")
        print("\t\t3. Random Poem\t\t\t\t\t7. Poem by Title")
        print("\t\t4. Poem by Line\t\t\t\t\t8. Exit")

        print("-"*96)
        choice = input("Enter your choice: ")
        print("-"*96)

        match choice:
            case "1":
                print(random_authors())

            case "2":
                print(random_titles())

            case "3":
                print(random_poem())

            case "4":
                line = input("Enter line: ").strip()
                print("-"*96)
                print(poem_by_line(line))

            case "5":
                linecount = input("Enter number of lines: ").strip()
                print("-"*96)
                print(poem_by_linecount(linecount))

            case "6":
                author_name = input("Enter author name: ").strip()
                print("-"*96)
                print(poem_by_author(author_name))

            case "7":
                poem_title = input("Enter poem title: ").strip()
                print("-"*96)
                print(poem_by_title(poem_title))

            case "8":
                break

            case _:
                print("Error: Incorrect Choice")


def random_authors():
    api = "https://poetrydb.org/author"
    response = requests.get(api).json()
    authors = response["authors"]
    random.shuffle(authors)
    for i in range(25):
        print(f"{i+1} - {authors[i]}")
    return the_end


def random_titles():
    api = "https://poetrydb.org/title"
    response = requests.get(api).json()
    titles = response["titles"]
    random.shuffle(titles)
    for i in range(25):
        print(f"{i+1} - {titles[i]}")
    return the_end


def random_poem():
    api = f"https://poetrydb.org/random"
    response = requests.get(api).json()
    lines = response[0]["lines"]
    cowsay.cow("\n".join(lines))
    return the_end


def poem_by_line(line):
    try:
        api = f"https://poetrydb.org/lines/{line}"
        response = requests.get(api).json()
        lines = response[0]["lines"]
        cowsay.cow("\n".join(lines))
        return the_end
    except:
        return "Poem Not Found"


def poem_by_linecount(lc):
    try:
        api = f"https://poetrydb.org/linecount/{lc}"
        response = requests.get(api).json()
        lines = response[0]["lines"]
        cowsay.cow("\n".join(lines))
        return the_end
    except:
        return "Poem Not Found"


def poem_by_author(author):
    try:
        api = f"https://poetrydb.org/author/{author}"
        response = requests.get(api).json()
        lines = response[0]["lines"]
        cowsay.cow("\n".join(lines))
        return the_end
    except:
        return "Author Not Found"


def poem_by_title(title):
    try:
        api = f"https://poetrydb.org/title/{title}"
        response = requests.get(api).json()
        lines = response[0]["lines"]
        cowsay.cow("\n".join(lines))
        return the_end
    except:
        return "Title Not Found"


if __name__ == "__main__":
    main()
