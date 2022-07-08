# https://wiki.python.org.br/EstruturaDeRepeticao

import numpy

number_iteration = int(input("How much iterations want make: "))
counter = int(0)
ages = []

while counter != number_iteration:
    ageInput = int(input("How old are you: "))
    ages.append(ageInput)
    counter += 1
average_age = numpy.median(ages)
if 0 < average_age <= 25:
    print(f"The medium is \033[34m{average_age:.0f}\033[38m the group is Young")
if 25 < average_age <= 60:
    print(f"The medium is \033[34m{average_age:.0f}\033[38m the group is Adult")
if average_age > 60:
    print(f"The medium is \033[34m{average_age:.0f}\033[38m the group is old")
