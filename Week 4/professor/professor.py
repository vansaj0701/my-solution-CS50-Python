import random


def main():
    level = get_level()
    score = 0
    chances = 0
    problem = 0

    while (problem < 10):
        if chances == 0:
            generate_integer(level)

        user_prompt = f"{str(random_num1)} + {str(random_num2)} = "

        try:
            user_answer = int(input((user_prompt)))
            if user_answer == answer:
                score += 1
                problem += 1
                chances = 0
                print(score)

            else:
                raise ValueError

        except ValueError:
            chances += 1
            print("EEE")
            if chances == 3:
                print(f"{user_prompt}{answer}")
                chances = 0
                problem += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    global random_num1, random_num2, answer

    if level == 1:
        random_num1 = random.randint(0, 9)
        random_num2 = random.randint(0, 9)

    elif level == 2:
        random_num1 = random.randint(10, 99)
        random_num2 = random.randint(10, 99)

    else:
        random_num1 = random.randint(100, 999)
        random_num2 = random.randint(100, 999)

    answer = random_num1 + random_num2

    return answer


if __name__ == "__main__":
    main()
