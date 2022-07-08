# https://wiki.python.org.br/ExerciciosListas

import random

dice_list = list()
dice_list_support = list()
dice_list_copy = list()
dice_list_counter = [0, 0, 0, 0, 0, 0]

for dice in range(0, 100):
    for dice_played in range(0, 6):
        dice_list_support.append(random.randint(0, 6))

    dice_list_copy = dice_list_support.copy()
    dice_list.append(dice_list_copy)
    dice_list_support.clear()

for number in range(0, len(dice_list)):
    for dice in range(0, 6):
        if dice_list[number][dice] == 1:
            dice_list_counter[0] += 1
        if dice_list[number][dice] == 2:
            dice_list_counter[1] += 1
        if dice_list[number][dice] == 3:
            dice_list_counter[2] += 1
        if dice_list[number][dice] == 4:
            dice_list_counter[3] += 1
        if dice_list[number][dice] == 5:
            dice_list_counter[4] += 1
        if dice_list[number][dice] == 6:
            dice_list_counter[5] += 1


for number in range(0, len(dice_list_counter)):
    print(f"\033[38mNumber {number + 1}\033[38m: \033[34m{dice_list_counter[number]}\033[38m")
