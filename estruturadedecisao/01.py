# https://wiki.python.org.br/EstruturaDeDecisao

first_number = str(input("First number: "))
second_number = str(input("Second number: "))

if first_number.isnumeric() is True and second_number.isnumeric() is True:
    if first_number > second_number:
        print(f"\033[34m{first_number}\033[38m is bigger than the \033[34m{second_number}\033[38m")
    elif second_number > first_number:
        print(f"\033[34m{second_number}\033[38m is bigger than the \033[34m{first_number}\033[38m")
    elif first_number == second_number:
        print(f"\033[34m{first_number}\033[38m is the same as the \033[34m{second_number}\033[38m")
else:
    print("\033[38mType just numbers")
