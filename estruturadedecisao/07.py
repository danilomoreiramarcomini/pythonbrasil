# https://wiki.python.org.br/EstruturaDeDecisao

first_number = float(input("Number: "))
second_number = float(input("Number: "))
third_number = float(input("Number: "))

if first_number > second_number and first_number > third_number:
    if second_number > third_number:
        print(f'The \033[34m{first_number}\033[38m is greater than \033[34m{second_number}\033[38m and \033[34m'
              f'{third_number}')
    else:
        print(f'The \033[34m{first_number}\033[38m is greater than \033[34m{third_number}\033[38m and \033[34m'
              f'{second_number}')
if second_number > first_number and second_number > third_number:
    if first_number > third_number:
        print(f'The \033[34m{second_number}\033[38m is greater than \033[34m{first_number}\033[38m and \033[34m'
              f'{third_number}')
    else:
        print(f'The \033[34m{second_number}\033[38m is greater than \033[34m{third_number}\033[38m and \033[34m'
              f'{first_number}')
if third_number > first_number and third_number > second_number:
    if first_number > second_number:
        print(f'The \033[34m{third_number}\033[38m is greater than \033[34m{first_number}\033[38m and \033[34m'
              f'{second_number}')
    else:
        print(f'The \033[34m{third_number}\033[38m is greater than \033[34m{second_number}\033[38m and \033[34m'
              f'{first_number}')
