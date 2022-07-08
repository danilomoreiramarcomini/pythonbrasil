# https://wiki.python.org.br/ExerciciosListas

my_list = list()
for element in range(0, 5):
    my_list.append(int(input("Enter with a number: ")))
for number in my_list:
    print(f"\033[34m{number}\033[34m", end=" ")
