# https://wiki.python.org.br/EstruturaDeRepeticao

number_by_input = int(input("Enter with the number of N terms: "))
numbers = []
sum_number = []
h = int(1)
for number in range(h, number_by_input + 1, 1):
    numbers.append(number)
for element in numbers:
    sum_number.append(h / element)
print(f"\033[34m{sum(sum_number):.2f}")
