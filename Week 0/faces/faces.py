#DEFINE CONVERT
def convert(str):
    #REPLACE :)-->🙂 AND :(-->🙁
    replacement = str.replace(":)", "🙂").replace(":(", "🙁")

    #RETURNING "replacement"
    return replacement

#DEFINE MAIN
def main():
    #INPUT TEXT FROM USER AND SAVING IT TO "text" VARIABLE
    #REMOVE WHITESPACES
    text = input("Enter text: ").strip()

    #PRINT TEXT
    print(f"Converted text: {convert(text)}")

main()
