# https://wiki.python.org.br/EstruturaDeRepeticao

number = int(input("Insert a number here: "))
numbers = []
for element in range(number, 0, -1):
    numbers.append(element)
print(f"\033[34m{number}\033[38m!", end="")

support = numbers[0]
for element in range(1, len(numbers)):
    support = support * numbers[element]

print(f" = \033[34m{support}")
