# https://wiki.python.org.br/EstruturaSequencial

import math

side = float(input("Enter the number of one of the sides of the square: "))
two = int(2)
area_of_square = math.pow(side, two)
twice_the_area_of_the_square = area_of_square * two
print(f"\033[38mThe area of square equals to \033[34m{area_of_square}\n\033[38mThe twice the area of square equals to "
      f"\033[34m{twice_the_area_of_the_square}\033[38m")
