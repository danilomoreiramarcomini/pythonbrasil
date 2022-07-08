# https://wiki.python.org.br/EstruturaDeRepeticao

import datetime

salary_initial = float(input("Insert the salary initial $: "))
current_year = datetime.datetime.today().year
print(f"Salary $:\033[34m{salary_initial:.2f}\033[38m Year: \033[34m1995\033[38m")
counter = 0
for year in range(1995, current_year):
    salary_initial = ((salary_initial * (0.15 / 100)) + salary_initial)
    counter += 1
    print(f"Salary $:\033[34m{salary_initial:.2f}\033[38m Year: \033[34m{1995 + counter}\033[38m")
