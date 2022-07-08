# https://wiki.python.org.br/ExerciciosListas

list_height = list()
list_age = list()
for people in range(1, 6):
    list_height.append(float(input(f"Enter with the weight for \033[34m{people}\033[38mª people: ")))
    list_age.append(int(input(f"Enter with the age for \033[34m{people}\033[38mª people: ")))
list_height.sort(reverse=True)
list_age.sort(reverse=True)
print('-' * 40)
for people in range(0, len(list_age)):
    print(f"\033[34m{people +1}\033[38mª People - Height: \033[34m{list_height[people]:.2f}\033[38m Age: \033[34m"
          f"{list_age[people]}\033[38m yo")
    print('-' * 40)
