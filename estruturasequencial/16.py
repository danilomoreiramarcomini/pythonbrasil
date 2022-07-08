# https://wiki.python.org.br/EstruturaSequencial

import math

area = float(input("Size in square meters: "))
area_of_ink = area / 3
numbers_of_cans = math.ceil(area_of_ink / 18)
pay = numbers_of_cans * 80

print(f"You will need \033[34m{numbers_of_cans}\033[38m cans for \033[34m{area}\033[38m² "
      f"You will pay $:\033[34m{pay:.2f}\033[38m")
