# https://wiki.python.org.br/EstruturaDeDecisao

result_of_fruit = int(input("Fruits:\n[1] Strawberry\n[2] Apple\nWrite here: "))

if result_of_fruit == 1:
    amount_of_strawberry = float(input("Write the amount of strawberry: "))
    if amount_of_strawberry <= 5:
        value_strawberry = 2.5
        total_price = (amount_of_strawberry * value_strawberry)
        print(f"\033[34m{amount_of_strawberry}\033[38m kilogram of Strawberry\nPay $:\033[34m{total_price:.2f}\033[38m")

    else:
        value_strawberry = 2.2
        total_price = (amount_of_strawberry * value_strawberry)
        if amount_of_strawberry > 8 or total_price > 25:
            new_total_price = (total_price - (total_price * 0.10))
            print(f"\033[34m{amount_of_strawberry}\033[38m kilogram of Strawberry\nPay $:\033[34m{new_total_price:.2f}"
                  f"\033[38m")
        else:
            print(f"\033[34m{amount_of_strawberry}\033[38m kilogram of Strawberry\nPay $:\033[34m{total_price:.2f}"
                  f"\033[38m")

if result_of_fruit == 2:
    amount_of_apple = float(input("Write the amount of apple: "))
    if amount_of_apple <= 5:
        value_apple = 1.8
        total_price = (amount_of_apple * value_apple)
        print(f"\033[34m{amount_of_apple}\033[38m kilogram of Apple\nPay $:\033[34m{total_price:.2f}\033[38m")

    else:
        value_apple = 1.5
        total_price = (amount_of_apple * value_apple)
        if amount_of_apple > 8 or total_price > 25:
            new_total_price = (total_price - (total_price * 0.10))
            print(f"\033[34m{amount_of_apple}\033[38m kilogram of Apple\nPay $:\033[34m{new_total_price:.2f}\033[38m")
        else:
            print(f"\033[34m{amount_of_apple}\033[38m kilogram of Apple\nPay $:\033[34m{total_price:.2f}\033[38m")
