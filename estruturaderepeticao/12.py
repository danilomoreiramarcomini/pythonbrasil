# https://wiki.python.org.br/EstruturaDeRepeticao

number = int(input("Write a number between 1 and 10: "))
while number < 1 or number > 10:
    number = int(input("Write a number between 1 and 10: "))
for element in range(1, 11, 1):
    print(f"\033[34m{number}\033[38m x \033[34m{element}\033[38m = \033[34m{number * element}")
