# https://wiki.python.org.br/EstruturaDeRepeticao

first_number = int(input("Enter with number interge: "))
second_number = int(input("Enter with other number interge: "))

if second_number > first_number:
    support = first_number
    first_number = second_number
    second_number = support
    for value in range(second_number, first_number, 1):
        print(value)
else:
    for value in range(second_number, first_number, 1):
        print(value)
print(f"The sum beetwen numbers \033[34m{first_number}\033[38m and \033[34m{second_number}\033[38m is \033[34m"
      f"{first_number + second_number}\033[38m")
