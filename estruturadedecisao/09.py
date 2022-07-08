# https://wiki.python.org.br/EstruturaDeDecisao

first_number = float(input("Number: "))
second_number = float(input("Number: "))
third_number = float(input("Number: "))

if first_number > second_number and first_number > third_number:
    if second_number > third_number:
        print(f"\033[34m{first_number}\n{second_number}\n{third_number}\033[38m")
    else:
        print(f"\033[34m{first_number}\n{third_number}\n{second_number}\033[38m")

elif second_number > first_number and second_number > third_number:
    if first_number > third_number:
        print(f'\033[34m{second_number}\n{first_number}\n{third_number}\033[38m')
    else:
        print(f"\033[34m{second_number}\n{third_number}\n{first_number}\033[38m")
elif third_number > first_number and third_number > second_number:
    if first_number > second_number:
        print(f"\033[34m{third_number}\n{first_number}\n{second_number}\033[38m")
    else:
        print(f"\033[34m{third_number}\n{second_number}\n{first_number}\033[38m")
