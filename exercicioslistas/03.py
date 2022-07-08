# https://wiki.python.org.br/ExerciciosListas

notes = list()
average = list()

for note in range(0, 4):
    notes.append(float(input(f"Enter with \033[34m{note + 1}\033[38mª note: ")))
average.append(sum(notes) / len(notes))

for element in notes:
    print(f"\033[34m{notes.index(element) + 1}\033[38mª Note: \033[34m{element:.1f}\033[38m")

print(f"Average: \033[34m{average[0]:.1f}\033[38m")
