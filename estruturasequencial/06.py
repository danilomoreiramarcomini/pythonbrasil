# https://wiki.python.org.br/EstruturaSequencial

import math

radius = float(input("Radius: "))
area = math.pi * math.pow(radius, 2)
print(f"\033[38mThe area of the circle is equivalent to \033[34m{area:.2f}\033[38m")
