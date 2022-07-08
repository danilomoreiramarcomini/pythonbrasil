# https://wiki.python.org.br/ExerciciosListas

import random

list_a = list()
list_b = list()
list_c = list()

for number in range(0, 10):
    list_a.append(random.randint(0, 1000))
    list_b.append(random.randint(0, 1000))

for number in range(0, 10):
    list_c.append(list_a[number])

for number in range(0, 10):
    list_c.append(list_b[number])
list_c.sort()
for number in list_c:
    print(f"\033[34m{number}\033[38m", end=" ")
