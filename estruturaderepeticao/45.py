# https://wiki.python.org.br/EstruturaDeRepeticao

from statistics import median

total = []
lesson_model = []
lesson_student = []
counter = int(0)
support = int(0)
point = int(0)
while True:
    support += 1
    lesson_model_by_input = str(input(f"Enter with answer of \033[34m{support}\033[38mº question: ")).upper()
    lesson_model.append(lesson_model_by_input)
    if len(lesson_model) == 10:
        while True:
            next_student = int(input(f"Do you want make to test now [1] Yes [2] No: "))
            if next_student == 1:
                for question in range(0, 10):
                    lesson_student_by_input = str(input(f"Enter with the answer for \033[34m{question + 1}\033[38mº: "))\
                        .upper()
                    lesson_student.append(lesson_student_by_input)
                    if lesson_student_by_input == lesson_model[question]:
                        point += 1
                total.append(point)
                point = 0
                counter += 1
            if next_student == 2:
                print(
                    f"The averages of students are \033[34m{median(total)}\033[38m and lower note is \033[34m"
                    f"{min(total)}\033[38m and the bigger note is \033[34m{max(total)}\033[38m\nStudents that made the "
                    f"test \033[34m{counter}\033[38m")
                break
        break
