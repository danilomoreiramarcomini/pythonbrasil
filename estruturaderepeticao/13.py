# https://wiki.python.org.br/EstruturaDeRepeticao

base = int(input("Insert a base: "))
exponent = int(input("Insert the exponent: "))

counter = int(1)
potency = int(1)
while True:
    if counter <= exponent:
        potency *= base
        counter += 1
    else:
        print(f"\033[34m{potency}")
        break
