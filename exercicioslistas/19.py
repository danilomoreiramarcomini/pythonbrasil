# https://wiki.python.org.br/ExerciciosListas

list_os = list()
for os in range(0, 6):
    list_os.append(1)

while True:
    choice_os = int(input("Vote in some OS: "))

    if choice_os == 1:
        list_os[0] += 1
    if choice_os == 2:
        list_os[1] += 1
    if choice_os == 3:
        list_os[2] += 1
    if choice_os == 4:
        list_os[3] += 1
    if choice_os == 5:
        list_os[4] += 1
    if choice_os == 6:
        list_os[5] += 1
    elif choice_os == 0:
        break

print(f"Operational System......Votes......Percentage")
print(f"Windows Server..........\033[34m{list_os[0]}\033[38m..........\033[34m"
      f"{100 / (sum(list_os) / list_os[0] - 1):.0f}\033[38m%")
print(f"Unix....................\033[34m{list_os[1]}\033[38m..........\033[34m"
      f"{100 / (sum(list_os) / list_os[1] - 1):.0f}\033[38m%")
print(f"Linux...................\033[34m{list_os[2]}\033[38m..........\033[34m"
      f"{100 / (sum(list_os) / list_os[2] - 1):.0f}\033[38m%")
print(f"Netware.................\033[34m{list_os[3]}\033[38m..........\033[34m"
      f"{100 / (sum(list_os) / list_os[3] - 1):.0f}\033[38m%")
print(f"Mac OS..................\033[34m{list_os[4]}\033[38m..........\033[34m"
      f"{100 / (sum(list_os) / list_os[4] - 1):.0f}\033[38m%")
print(f"Others..................\033[34m{list_os[5]}\033[38m..........\033[34m"
      f"{100 / (sum(list_os) / list_os[5] - 1):.0f}\033[38m%")
