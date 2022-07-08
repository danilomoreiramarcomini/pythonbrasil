# https://wiki.python.org.br/EstruturaDeRepeticao

first_number = int(input("Enter with number interge: "))
second_number = int(input("Enter with other number interge: "))

if second_number > first_number:
    support = first_number
    first_number = second_number
    second_number = support
    for value in range(second_number, first_number, 1):
        print(f"\033[34m{value}")
else:
    for value in range(second_number, first_number, 1):
        print(f"\033[34m{value}")
