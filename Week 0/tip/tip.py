def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #REMOVE '$' SIGN
    #CONVERT TO FLOAT
    meal_price = float(d.replace("$",""))

    #ROUND TO ONE DECIMAL PLACES
    rounded_meal_price = round(meal_price,1)

    #RETURN "rounded_meal_price"
    return rounded_meal_price


def percent_to_float(p):
    #REMOVE "%" SIGN
    #CONVERT TO FLOAT
    tip_percent = float(p.replace("%",""))

    #EXAMPLE: 15-->0.15
    tip_percent_decimal = tip_percent / 100

    #RETURN tip_percent_decimal
    return tip_percent_decimal

main()
