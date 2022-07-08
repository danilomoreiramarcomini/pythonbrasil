# https://wiki.python.org.br/EstruturaDeRepeticao

from math import ceil

amount_turm = int(input("How many turms you will create: "))
amount_students = int(input("The amount of students for turm: "))
turms = []
students = []
if amount_students <= 40:
    for turm in range(1, amount_turm + 1):
        turm_by_input = str(input(f"Insert the name of \033[34m{turm}\033[38mº turm: "))
        turms.append(1)
        for student in range(1, amount_students + 1):
            student_by_input = str(input(f"Inser the name of \033[34m{student}\033[38mº student: "))
            students.append(1)
    print(f"The median of students for class is \033[34m{ceil(sum(students) / sum(turms))}\033[38m")

else:
    print("The amount of students can't be bigger to 40")
