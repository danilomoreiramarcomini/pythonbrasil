# https://wiki.python.org.br/ExerciciosListas

my_list = list()
list_support = list()
for number in range(1, 11):
    my_list.append(int(input("'Enter with the \033[34m{number}\033[38mº: ")))

for number in range(0, len(my_list)):
    list_support.append(my_list[number] * my_list[number])

my_list.clear()
my_list = list_support

for number in my_list:
    print(f"\033[34m{number}\033[38m", end=" ")
