# https://wiki.python.org.br/EstruturaDeRepeticao

from sympy import isprime

number_by_input = int(input("Insert a number here: "))
counter = int(0)
for number in range(1, number_by_input):
    support = isprime(number)
    if support is True:
        print(f"{number}")
        counter += 1
print(f"The program has maked \033[34m{counter} \033[38mdivisons")
