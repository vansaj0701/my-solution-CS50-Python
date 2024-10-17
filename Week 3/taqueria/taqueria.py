menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total_price = 0
    while True:
        try:
            item_name = input("Item: ").strip().title()
            item_price = price(item_name)
            if item_price:
                total_price += item_price
                print(f"Total: ${total_price:.2f}")
            else:
                continue
        except EOFError:
            break


def price(item_name):
    for key, value in menu.items():
        if item_name == key:
            return value
        else:
            continue

main()
