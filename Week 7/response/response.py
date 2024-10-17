from validator_collection import validators, errors


def main():
    email_input = input("What's your email address?")
    if email_validate(email_input):
        print("Valid")
    else:
        print("Invalid")


def email_validate(email):
    try:
        email_validation = validators.email(email)
    except (ValueError, errors.EmptyValueError, errors.InvalidEmailError):
        return False

    return True


if __name__ == '__main__':
    main()
