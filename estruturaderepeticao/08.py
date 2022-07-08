# https://wiki.python.org.br/EstruturaDeRepeticao

numbers = []
for number in range(1, 6, 1):
    numberInput = float(input("Insert a number here: "))
    numbers.append(numberInput)

print(f"\033[38mThe sum is \033[34m{sum(numbers):.2f}")
print(f"\033[38mThe mean is \033[34m{sum(numbers) / len(numbers):.2f}")
