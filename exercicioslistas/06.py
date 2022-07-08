# https://wiki.python.org.br/ExerciciosListas

notes = list()
list_support = list()
list_copy = list()
list_average = list()
for student in range(1, 11):
    print(f"Notes of {student}º student")
    for note in range(1, 5):
        list_support.append(float(input(f"Enter with \033[34m{note}\033[38mª note: ")))

    list_copy = list_support.copy()
    notes.append(list_copy)
    list_support.clear()

for element in range(0, len(notes)):
    list_average.append(sum(notes[element]) / (len(notes[element])))

for student in list_average:
    if student >= 7:
        list_support.append(student)

print(f"\033[34m{len(list_support)}\033[38m")
