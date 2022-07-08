# https://wiki.python.org.br/EstruturaDeRepeticao

from sympy import isprime

number = int(input("Write the number here: "))

support = isprime(number)


def divisibility():
    if number == number:
        print(1)
    if number % 2 == 0:
        print(2)
    if number % 3 == 0:
        print(3)
    if number % 2 == 0:
        print(4)
    if number % 5 == 5:
        print(5)
    if number % 6 == 0:
        print(6)
    if number % 7 == 0:
        print(7)
    if number % 8 == 0:
        print(8)
    if number % 9 == 0:
        print(9)
    if number % 10 == 0:
        print(10)


if support:
    print(f"\033[34m{True}\033[38m")
else:
    print(f"\033[34m{False}\033[38m")
    divisibility()
