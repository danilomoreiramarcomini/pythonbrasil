# https://wiki.python.org.br/EstruturaDeDecisao

import statistics

first_note = float(input("First note: "))
second_note = float(input("Second note: "))
average = statistics.fmean([first_note, second_note])

if average >= 9:
    print(f"Approved! Your classification: A\n"
          f"The notes was \033[34m{first_note}\033[38m and \033[34m{second_note}\033[38m"
          f" Your average \033[34m{average}\033[38m")

elif 7.5 <= average < 9:
    print(f"Approved! Your classification: \033[34mB\033[38m\n\n"
          f"The notes was \033[34m{first_note}\033[38m and \033[34m{second_note}\033[38m"
          f" Your average \033[34m{average}\033[38m")

elif 6 <= average < 7.5:
    print(f"Approved! Your classification: \033[34mC\033[38m\n\n"
          f"The notes was \033[34m{first_note}\033[38m and \033[34m{second_note}\033[38m"
          f" Your average \033[34m{average}\033[38m")

elif 4 <= average < 6:
    print(f"Reproved! Your classification: \033[34mD\033[38m\n\n"
          f"The notes was \033[34m{first_note}\033[38m and \033[34m{second_note}\033[38m"
          f" Your average \033[34m{average}\033[38m")

elif average < 4:
    print(f"Reproved! Your classification: \033[34mE\033[38m\n\n"
          f"The notes was \033[34m{first_note}\033[38m and \033[34m{second_note}\033[38m"
          f" Your average \033[34m{average}\033[38m")
