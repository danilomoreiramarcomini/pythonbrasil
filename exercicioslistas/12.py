# https://wiki.python.org.br/ExerciciosListas

import random

list_height = list()
list_age = list()
counter = int(0)
for student in range(0, 30):
    list_height.append(round(random.uniform(1.00, 2.00), 2))
    list_age.append(random.randint(10, 17))

average = float(sum(list_height) / len(list_height))
average = round(average, 2)

for student in range(len(list_age)):
    if list_age[student] > 13:
        if list_height[student] < average:
            counter += 1
    else:
        x = 1

print(f"\033[34m{counter}\033[38m students are below average height")

for student in range(len(list_age)):
    print(f"\033[34m{list_height[student]:.2f}\033[38m and \033[34m{list_age[student]}\033[38m")

print(f"\033[38mThe Average:\033[34m{average}\033[38m")
