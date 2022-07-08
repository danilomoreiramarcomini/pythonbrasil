# https://wiki.python.org.br/EstruturaSequencial

first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = float(input("Third number: "))
twice_of_first_number = int(first_number + first_number)
half_of_the_second_number = int(second_number / 2)
sum_of_triple_the_first_number_with_third_number = ((first_number * 3) + third_number)
print(f'\033[38ma. \033[34m{twice_of_first_number * half_of_the_second_number}')
print(f'\033[38mb. \033[34m{sum_of_triple_the_first_number_with_third_number}')
print(f'\033[38mc. \033[34m{third_number ** 3}')
