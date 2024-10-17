# DEFINE FUNCTION "bank"
def bank(greeting):
    # CONDITIONS FOR GREETING
    if (greeting.startswith("hello")):
        return "$0"

    elif (greeting.startswith("h")):
        return "$20"

    else:
        return "$100"


# DEFINE FUNCTION "main"
def main():
    # INPUT GREETING FROM USER AND SAVE IT TO "greet" VARIABLE
    # REMOVE ANY LEADING WHITESPACE AND CONVERT TO LOWERCASE
    greet = input("Greeting: ").strip().lower()
    print(f"You got {bank(greet)}")


# FUNCTION CALL
main()
