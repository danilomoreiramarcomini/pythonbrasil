# https://wiki.python.org.br/ExerciciosListas

import random

months_tuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December")
temperature_list = list()
for temperature in range(0, 12):
    temperature_list.append(round(random.uniform(-5, 42), 1))
annual_average = float(sum(temperature_list) / len(temperature_list))
annual_average = round(annual_average, 1)
print('-' * 50)

for temperature in range(len(temperature_list)):
    if temperature_list[temperature] > annual_average:
        print(f"\033[34m{months_tuple[temperature]}\033[38m: \033[34m{temperature_list[temperature]}\033[38mºC")
        print("-" * 50)
print(f"Annual Average: \033[34m{annual_average}\033[38mºC")
