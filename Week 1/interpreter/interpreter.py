# DEFINE FUNCTION math
def math(num1, operand, num2):

    # CHECK FOR OPERAND
    match operand:
        case "+":
            return num1 + num2
        case "-":
            return num1-num2
        case "/":
            if num2 == 0:
                return "can't divide by zero"
            else:
                return num1/num2
        case "*":
            return num1*num2
        case _:
            return False


# DEFINE function main
def main():
    # INPUT EXPRESSION FROM USER AND SAVE IT TO "exp" VARIABLE
    exp = input("Expression: ")

    # SPLIT EXPRESSION
    x, y, z = exp.split(" ")

    # PRINT AND CALL math FUNCTION
    print(math(float(x), y, float(z)))


# CALL main FUNCTION
main()
