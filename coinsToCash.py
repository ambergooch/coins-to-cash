def calc_dollars():
    piggyBank = {
        "pennies": 342,
        "nickels": 95,
        "dimes": 32,
        "quarters": 86
    }
    pennies = piggyBank["pennies"] / 100
    nickels = piggyBank["nickels"] / 20
    dimes = piggyBank["dimes"] / 10
    quarters = piggyBank["quarters"] / 4
    dollarAmount = pennies + nickels + dimes + quarters
    print(round(dollarAmount, 2))

calc_dollars()
