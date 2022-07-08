# https://wiki.python.org.br/ExerciciosListas

print(f"1 - Need sphere\n"
      f"2 - Need Clean\n"
      f"3 - Need cable or connector\n"
      f"4 - Broke")
tuple_name = ("Need spehre", "Need Clean", "Need cable or connector", "Broke")
list_mouse = list()
for element in range(0, 4):
    list_mouse.append(0)

while True:
    select_option = int(input("Select a option: "))
    if select_option == 0:
        break
    if select_option == 1:
        amountMouse = int(input("Amount mouses: "))
        list_mouse[0] += amountMouse
    if select_option == 2:
        amountMouse = int(input("Amount mouses: "))
        list_mouse[1] += amountMouse
    if select_option == 3:
        amountMouse = int(input("Amount mouses: "))
        list_mouse[2] += amountMouse
    if select_option == 4:
        amountMouse = int(input("Amount mouses: "))
        list_mouse[3] += amountMouse
print(f"Amount mouses: \033[34m{sum(list_mouse)}\033[38m")
print(f"Condition - Amount")
for mouse in range(0, len(list_mouse)):
    print(f"\033[34m{tuple_name.index(tuple_name[mouse]) + 1}\033[38m"
          f" - \033[34m{tuple_name[mouse]}\033[38m"
          f" - \033[34m{list_mouse[mouse]}\033[38m")
    print(f"\033[34m{100/(sum(list_mouse) / list_mouse[mouse]):.2f}\033[38m%")
