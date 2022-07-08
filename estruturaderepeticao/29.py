# https://wiki.python.org.br/EstruturaDeRepeticao

amount_products = int(input("Insert here the amount products buyed: "))
price_products = float(input("Insert the number of product $: "))
value_product = float(0)
if amount_products <= 50:
    for product in range(1, amount_products + 1):
        print(f"Apu Market - Price List\n\033[38m{product}\033[38m - $:\033[34m{price_products * product}\033[38m")

else:
    print("The amount can't bigger than 50")
