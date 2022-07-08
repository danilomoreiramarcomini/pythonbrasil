# https://wiki.python.org.br/EstruturaDeRepeticao

hot_dog_counter = int(0)
simples_bauru_counter = int(0)
bauru_with_egg_counter = int(0)
hamburger_counter = int(0)
cheese_burger_counter = int(0)
refrigerant_counter = int(0)

price_hot_dog = float(1.20)
price_simples_bauru = float(1.30)
price_bauru_with_egg = float(1.50)
price_hamburger = float(1.20)
price_cheese_burger = float(1.30)
price_refrigerant = float(1.00)
print("Specification..Code.Price\n"
      "Hot Dog........100..$:1.20\n"
      "Simples Bauru..101..$:1.30\n"
      "Bauru with Egg.102..$:1.50\n"
      "Hamburger......103..$:1.20\n"
      "CheeseBurger...104..$:1.30\n"
      "Refrigerant....105..$:1.00")

while True:

    code = int(input("Enter with the code: "))
    amount_product = int(input(f"Enter with the amount: "))
    if code == 100:
        hot_dog_counter += amount_product

    if code == 101:
        simples_bauru_counter += amount_product

    if code == 102:
        bauru_with_egg_counter += amount_product

    if code == 103:
        hamburger_counter += amount_product

    if code == 104:
        cheese_burger_counter += amount_product

    if code == 105:
        refrigerant_counter += amount_product

    if code == 0:
        total_hot_dog = float(price_hot_dog * hot_dog_counter)
        total_simples_bauru = float(price_simples_bauru * simples_bauru_counter)
        total_bauru_with_egg = float(price_bauru_with_egg * bauru_with_egg_counter)
        total_hamburger = float(price_hamburger * hamburger_counter)
        total_cheese_burger = float(price_cheese_burger * cheese_burger_counter)
        total_refrigerant = float(price_refrigerant * refrigerant_counter)
        total = float(total_hot_dog + total_simples_bauru + total_bauru_with_egg + total_hamburger +
                      total_cheese_burger + total_refrigerant)

        print(f"\033[34m{hot_dog_counter}\033[38m.Hot dog.........$:\033[34m{total_hot_dog:.2f}\n"
              f"\033[34m{simples_bauru_counter}\033[38m.Simples Bauru...$:\033[34m{total_simples_bauru:.2f}\n"
              f"\033[34m{bauru_with_egg_counter}\033[38m.Bauru with Egg..$:\033[34m{total_bauru_with_egg:.2f}\n"
              f"\033[34m{hamburger_counter}\033[38m.Hamburger.......$:\033[34m{total_hamburger:.2f}\n"
              f"\033[34m{cheese_burger_counter}\033[38m.CheeseBurger....$:\033[34m{total_cheese_burger:.2f}\n"
              f"\033[34m{refrigerant_counter}\033[38m.Refrigerant.....$:\033[34m{total_refrigerant:.2f}\n"
              f"\033[38mTotal\033[38m...$:\033[34m{total:.2f}")
        break
