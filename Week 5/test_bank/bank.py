# DEFINE FUNCTION "bank"
def value(greeting):
    # CONDITIONS FOR GREETING
    if (greeting.startswith("hello")):
        return 0

    elif (greeting.startswith("h") and not greeting.startswith("hello")):
        return 20

    else:
        return 100


# DEFINE FUNCTION "main"
def main():
    # INPUT GREETING FROM USER AND SAVE IT TO "greet" VARIABLE
    # REMOVE ANY LEADING WHITESPACE AND CONVERT TO LOWERCASE
    greet = input("Greeting: ").strip().lower()
    print(f"You got {value(greet)}")


# FUNCTION CALL
if __name__ == "__main__":
    main()
