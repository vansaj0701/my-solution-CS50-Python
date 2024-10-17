calories_dict = {
    15: ["lemon"],
    20: ["lime"],
    50: ["avocado", "cantaloupe", "honeydew melon", "pineapple", "strawberries", "tangerine"],
    60: ["grapefruit", "nectarine", "peach"],
    70: ["plums"],
    80: ["orange", "watermelon"],
    90: ["grapes", "kiwifruit"],
    100: ["pear", "sweet cherries"],
    110: ["banana"],
    130: ["apple"]
}


def calories(fruit):
    for i, j in calories_dict.items():
        if fruit in j:
            return i
        else:
            continue


def main():
    item = input("item: ").strip().lower()

    if calories(item):
        print(f"Calories: {calories(item)}")
    else:
        print()


main()
