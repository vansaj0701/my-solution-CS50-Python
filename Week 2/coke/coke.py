def main():
    amount_due = 50
    coke_price = 50
    total_amount = 0
    while (amount_due > 0):
        print(f"Amount Due: {amount_due}")
        amount = int(input("Insert Coin: "))
        if amount in (25,10,5):
            total_amount += amount
            if total_amount >= 50:
                print(f"Change Owed: {total_amount - coke_price}")
            amount_due -= amount
        else:
            print("Amount Invalid")
    return amount_due

main()
