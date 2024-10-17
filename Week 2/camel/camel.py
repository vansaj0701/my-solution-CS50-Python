# DEFINE FUNCTION "snake_case"
def snake_case(var):
    result = ""
    for char in var:
        if char.isupper():
            # ADD UNDERSCORE(US)
            add_under_score = "_" + char.lower()
            result += add_under_score

        else:
            result += char

    return result


# DEFINE FUNCTION "main"
def main():
    # INPUT VARIABLE NAME FROM USER AND SAVE IT TO "V_name" VARIABLE
    # REMOVE ANY LEADING WHITESPACE AND CONVERT TO LOWERCASE
    v_name = input("camelCase: ").strip()

    print(f"snake_case: {snake_case(v_name)}")


# FUNCTION CALL
main()
