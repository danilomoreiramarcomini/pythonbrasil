# https://wiki.python.org.br/EstruturaSequencial

import statistics

first_note = float(input("First note: "))
second_note = float(input("Second note: "))
third_note = float(input("Third note: "))
fourth_note = float(input("Fourth note: "))
average = statistics.mean([first_note, second_note, third_note, fourth_note])
print(f"\033[38mYour final average was \033[34m{average:.2f}")
