# https://wiki.python.org.br/ExerciciosListas

import random

list_a = list()
list_b = list()
list_c = list()
list_d = list()
for number in range(0, 10):
    list_a.append(random.randint(0, 1000))
    list_b.append(random.randint(0, 1000))
    list_c.append(random.randint(0, 1000))

for number in range(0, 10):
    list_d.append(list_a[number])

for number in range(0, 10):
    list_d.append(list_b[number])
list_d.sort()

for number in range(0, 10):
    list_d.append(list_c[number])
for number in list_d:
    print(f"\033[34m{number}\033[38m", end=" ")
