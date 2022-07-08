# https://wiki.python.org.br/EstruturaDeDecisao

from statistics import fmean

first_note = float(input("First note: "))
second_note = float(input("second note: "))
third_note = float(input("Third note: "))
notes_in_array = [first_note, second_note, third_note]
average = fmean(notes_in_array)

if average >= 7:
    print(f"\033[38mApproved!\nYour average: \033[34m{average:.2f}")
else:
    print(f"\033[38mReproved!\nYour average: \033[34m{average:.2f}")
