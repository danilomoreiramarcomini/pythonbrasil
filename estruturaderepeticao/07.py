# https://wiki.python.org.br/EstruturaDeRepeticao

numbers = []
for number in range(1, 6, 1):
    numberInput = int(input("Insert a number here: "))
    numbers.append(numberInput)

print(f"\033[34m{max(numbers)}")
