# https://wiki.python.org.br/EstruturaDeRepeticao

import math

numbers = []
number = int(input("Insert a number here: "))
numbers.append(number)
factor = number

for element in numbers:
    factor = factor - 1
    numbers.append(factor)
    if factor == 1:
        break
print(f"\033[38mThe factor of \033[34m{number}\033[38m! is \033[34m{math.prod(numbers)}")
