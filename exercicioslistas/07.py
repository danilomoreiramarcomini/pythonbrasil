# https://wiki.python.org.br/ExerciciosListas

my_list = list()
multiplication = int(1)
for number in range(1, 6):
    my_list.append(int(input(f"Enter with the \033[34m{number}\033[38mº number: ")))

print(f"The sum between numbers is \033[34m{sum(my_list)}\033[38m")
for number in my_list:
    multiplication = number * multiplication

print(f"The multiplication between number is \033[34m{multiplication}\033[38m")
for number in my_list:
    print(f"\033[34m{number}\033[38m", end=" ")
