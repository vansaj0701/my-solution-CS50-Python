from random import randint


def level_input():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            continue


def guess_input():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            continue


def random_number(level):
    return randint(1, level)


def guessing_game(random_num, guess):
    if guess > random_num:
        return "Too large!"
    elif guess < random_num:
        return "Too small!"
    else:
        return "Just right!"


def main():
    level = level_input()
    random_num = random_number(level)
    while True:
        guess = guess_input()
        result = guessing_game(random_num, guess)
        print(result)
        if result == "Just right!":
            break


if __name__ == "__main__":
    main()
