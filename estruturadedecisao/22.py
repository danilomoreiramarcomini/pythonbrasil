# https://wiki.python.org.br/EstruturaDeDecisao

number = int(input("Type a number: "))

if number % 2 == 0:
    print(f"\033[34m{number}\033[38m is evens")
else:
    print(f"\033[34m{number}\033[38m is odds")
