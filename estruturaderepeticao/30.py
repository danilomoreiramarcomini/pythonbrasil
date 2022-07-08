# https://wiki.python.org.br/EstruturaDeRepeticao

bread_price = float(input("Insert the bread price here $: "))
bread_amount = int(input("Insert the amount bread here: "))
if bread_amount <= 50:
    for bread in range(1, bread_amount + 1):
        print(f"{bread} - $:\033[34m{(bread_price * bread):.2f}\033[38m")

else:
    print("The amount can't bigger than 50")
