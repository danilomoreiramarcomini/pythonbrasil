# https://wiki.python.org.br/ExerciciosListas

print(f"ORGANIZATIONS TABAJARA")
print(f"=" * 22)
bonus_list = list()
salary_list = list()
counter = int(0)

while True:
    salary_by_input = float(input("Salary: "))
    if salary_by_input == 0:
        break
    else:
        salary_list.append(salary_by_input)

if 0 in salary_list:
    salary_list.remove(0)
for salary in salary_list:
    bonus = float(salary * 0.20)
    if bonus < 100:
        bonus = 100
        counter += 1
    bonus_list.append(bonus)
print(f"Salary - Bonus")
for salary in range(0, len(salary_list)):
    print(f"$: \033[34m{salary_list[salary]}\033[38m - $ \033[34m{bonus_list[salary]}\033[38m")


print(f"\033[34m{len(salary_list)}\033[38m employees")
print(f"Bonus total $:\033[34m{sum(bonus_list)}\033[38m")
print(f"Bonus min for \033[34m{counter}\033[38m employees")
print(f"Biggest bonus paid $:\033[34m{max(bonus_list)}\033[38m")
