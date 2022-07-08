# https://wiki.python.org.br/EstruturaDeRepeticao

first_counter = int(0)
second_counter = int(0)
third_counter = int(0)
fourth_counter = int(0)
while True:

    number = int(input("Type a number integer: "))
    if 0 <= number <= 25:
        first_counter += 1
    if 26 <= number <= 50:
        second_counter += 1
    if 51 <= number <= 75:
        third_counter += 1
    if 76 <= number <= 100:
        fourth_counter += 1

    if number < 0:
        print(f"Amount of numbers between 000 and 025:\033[34m{first_counter}\033[38m")
        print(f"Amount of numbers between 026 and 050:\033[34m{second_counter}\033[38m")
        print(f"Amount of numbers between 051 and 075:\033[34m{third_counter}\033[38m")
        print(f"Amount of numbers between 076 and 100:\033[34m{fourth_counter}\033[38m")
