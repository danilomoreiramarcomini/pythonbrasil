# https://wiki.python.org.br/EstruturaDeDecisao

import statistics

first_note = float(input("First note: "))
second_note = float(input("Type the second note: "))
average = statistics.mean([first_note, second_note])

if average == 10:
    print(f"Your average was \033[34m{average}\033[38m\n\033[34mApproved\033[38m with distinction!")

elif average >= 7:
    print(f"Your average was \033[34m{average}\033[38m\n\033[34mApproved\033[38m!")

elif average < 7:
    print(f"Your average was \033[34m{average}\033[38m\n\033[31mReproved\033[38m!")
