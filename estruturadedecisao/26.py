# https://wiki.python.org.br/EstruturaDeDecisao

choice = int(input("[1] Alcohol \n[2] Gasoline\nWrite here: "))

if choice == 1:
    amount = float(input("Amount of alcohol: "))
    value = 1.90
    if amount <= 20:
        amount_price_reduction = (amount * value) - ((amount * value) * 0.03)
        print(f"Value $:\033[34m{amount_price_reduction:.2f}\n\033[38mA-alcohol: \033[34m{amount:.2f}\033[38m liters")
    if amount > 20:
        amount_price_reduction = (amount * value) - ((amount * value) * 0.05)
        print(f"Value $:\033[34m{amount_price_reduction:.2f}\n\033[38mA-alcohol: \033[34m{amount:.2f}\033[38m liters")
if choice == 2:
    amount = float(input("Amount of gasoline: "))
    value = 2.50
    if amount <= 20:
        amount_price_reduction = (amount * value) - ((amount * value) * 0.04)
        print(f"Value $:\033[34m{amount_price_reduction:.2f}\n\033[38mG-gasoline: \033[34m{amount:.2f}\033[38m liters")
    if amount > 20:
        amount_price_reduction = (amount * value) - ((amount * value) * 0.06)
        print(f"Value $:\033[34m{amount_price_reduction:.2f}\n\033[38mG-gasoline: \033[34m{amount:.2f}\033[38m liters")
