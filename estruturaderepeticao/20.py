# https://wiki.python.org.br/EstruturaDeRepeticao

import math


def factorial():
    numbers = []
    number_by_input = int(input("Insert a number here: "))
    numbers.append(number_by_input)
    factor = number_by_input
    if number_by_input == 1:
        factorial()

    if 0 <= number_by_input <= 16:
        for element in numbers:
            factor = factor - 1
            numbers.append(factor)
            if factor == 1:
                break
        print(f"The factor of \033[34m{number_by_input}\033[38m! is \033[34m{math.prod(numbers)}\033[38m")
        print("You want continue?")
        choice_by_input = int(input("[1] - Yes [2] - No: "))
        if choice_by_input == 1:
            factorial()

        if choice_by_input != 1:
            print("Bye")
    else:
        factorial()


factorial()
