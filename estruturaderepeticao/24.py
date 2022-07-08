# https://wiki.python.org.br/EstruturaDeRepeticao
import numpy

numbers = []
number_of_iInterations = int(input("Insert the number of interations: "))

for element in range(1, number_of_iInterations + 1):
    numInput = int(input("Insert a number here: "))
    numbers.append(numInput)
print(f"\033[34m{numpy.median(numbers)}")
