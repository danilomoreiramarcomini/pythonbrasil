# https://wiki.python.org.br/ExerciciosListas

my_list = list()
counter = int(1)

while True:
    letter_by_input = str(input(f"Enter a \033[34m{counter}\033[38mª letters word: ")).upper()[0]
    letter_support = letter_by_input.isalpha()
    if letter_support is True:
        my_list.append(letter_by_input)
        counter += 1
    if len(my_list) == 10:
        break

for element in range(0, len(my_list)):
    support = my_list.index(my_list[element])
    letter = my_list[support]
    for letters in range(0, len(letter)):
        if letter[letters] not in "AEIOU":
            print(f"\033[34m{letter[letters]}\033[38m", end=" ")
