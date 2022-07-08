# https://wiki.python.org.br/EstruturaDeRepeticao

from sympy import isprime

number = int(input("Write the number here: "))
support = isprime(number)
if support:
    print(f"\033[34m{True}")
else:
    print(f"\033[31m{False}")
