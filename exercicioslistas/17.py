# https://wiki.python.org.br/ExerciciosListas

list_support = list()
my_list = list()
name_list = list()
copy_list = list()
counter = int(0)
support = int(0)
average_list = list()

while True:
    name_by_input = str(input("Enter the athlete's name:")).title()
    if name_by_input == "Q":
        break
    else:
        name_list.append(name_by_input)
        for jump in range(1, 6):
            list_support.append(float(input(f"\033[34m{jump}\033[38mº Jump: ")))

    copy_list = list_support.copy()
    my_list.append(copy_list)
    list_support.clear()

for athlete in name_list:
    print(f"Athlete:\033[34m{athlete}\033[38m\n")
    for jump in range(0, 5):
        print(f"The \033[34m{jump + 1}\033[38mº Jump: \033[34m{my_list[counter][jump]}\033[38m m")
    counter += 1

    print(f"Final result: ")
    print(f"Athlete:\033[34m{name_list[0 + support]}\033[38m")

    print(f"Jumps: \033[34m{my_list[support][0]}\033[38m - \033[34m{my_list[support][1]}\033[38m - \033[34m"
          f"{my_list[support][2]}\033[38m - \033[34m{my_list[support][3]}\033[38m - \033[34m{my_list[support][4]}"
          f"\033[38m")

    for element in range(0, len(my_list)):
        average_list.append(sum(my_list[element]) / len(my_list[element]))
    print(f"Average Jump:\033[34m{average_list[support]}")
    support += 1
    print('\n')
