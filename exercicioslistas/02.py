# https://wiki.python.org.br/ExerciciosListas

my_list = list()
for element in range(0, 10):
    my_list.append(int(input("Enter with a number: ")))
my_list.sort(reverse=True)
for number in my_list:
    print(f"\033[34m{number}\033[38m", end=" ")
