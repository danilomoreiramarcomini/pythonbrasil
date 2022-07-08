# https://wiki.python.org.br/ExerciciosListas

numbers = list()
evens = list()
odds = list()
for number in range(1, 21):
    numbers.append(int(input(f"Enter with \033[34m{number}\033[38mº number: ")))

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print("EVENS: ")
for number in evens:
    print(f"\033[34m{number}\033[38m", end=" ")
print(f"\nODDS: ")
for number in odds:
    print(f"\033[34m{number}\033[38m", end=" ")
