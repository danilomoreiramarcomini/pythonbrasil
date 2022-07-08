# https://wiki.python.org.br/EstruturaDeDecisao

number = int(input("Number: "))

if number >= 0:
    print(f"\033[34m{number}\033[38m is positive")
else:
    print(f"\033[34m{number}\033[38m is negative")
