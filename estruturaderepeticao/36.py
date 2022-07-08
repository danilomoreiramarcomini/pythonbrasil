# https://wiki.python.org.br/EstruturaDeRepeticao

times_table = int(input("Enter with number of times tables: "))
initial = int(input("Enter with number initial position: "))
finish = int(input("Enter with number final position: "))
if finish < initial:
    print("The initial position can't be bigger than final position")
else:
    for element in range(initial, finish + 1):
        print(f"\033[34m{times_table * initial}")
        initial += 1
