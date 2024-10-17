#DEFINE FUNCTION "answer"
def answer(ans):
    #CONDITION FOR ANSWER
    match ans:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


#DEFINE FUNCTION "main"
def main():
    #INPUT ANSWER FROM USER AND SAVE IT TO "ques" VARIABLE
    #REMOVE WHITESPACE AND CONVERT TO LOWERCASE
    ques = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()

    #CHECK WHETHER ANSWER IS "YES" OR "NO"
    if answer(ques):
        print("Yes")

    else:
        print("No")

#FUNCTION CALL
main()
