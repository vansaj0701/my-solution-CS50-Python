grocery = {}
sorted_grocery_dict = {}


def main():
    while True:
        try:
            grocery_items = input("").strip().lower()
            grocery_list(grocery_items)
        except EOFError:
            grocery_sorted(grocery)
            for key, value in sorted_grocery_dict.items():
                print(f"{value} {key.upper()}")
            break


def grocery_list(item):
    if item in grocery:
        grocery[item] += 1

    else:
        grocery[item] = 1

    return grocery


def grocery_sorted(item):
    sorted_dict = sorted(item.keys())

    for key in sorted_dict:
        sorted_grocery_dict[key] = grocery[key]

    return sorted_grocery_dict


main()
