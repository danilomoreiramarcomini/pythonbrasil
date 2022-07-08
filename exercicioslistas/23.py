# https://wiki.python.org.br/ExerciciosListas

names_list = ["Alexandre", "Anderson", "Antonio", "Carlos", "Cesar", "Rosemary"]
bytes_list = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]
megabytes_list = list()
percentage_list = list()


def convert():
    for byte in bytes_list:
        megabytes_list.append(float(byte / 1048576))


convert()


def percentage():
    for element in megabytes_list:
        percentage_list.append(100 / sum(megabytes_list) * element)


percentage()

for megabyte in range(0, len(bytes_list)):
    print(f"\033[34m{megabyte + 1} \033[38m{names_list[megabyte]}........"
          f"\033[34m{megabytes_list[megabyte]:.2f}\033[38m MB "
          f"\033[34m{percentage_list[megabyte]:.2f}\033[38m%")
