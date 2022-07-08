# https://wiki.python.org.br/EstruturaDeDecisao

initial_salary = float(input("Salary $: "))

if initial_salary <= 250:
    percentage_increase = (initial_salary * 0.20) + initial_salary
    print(f"Percentage increase: \033[34m20%\033[38m\n"
          f"Initial salary....$: \033[34m{initial_salary}\033[38m\n"
          f"Value of increase.$: \033[34m{initial_salary * 0.20}\033[38m\n"
          f"New salary........$: \033[34m{percentage_increase}\033[38m\n")

elif 250 < initial_salary <= 700:
    percentage_increase = (initial_salary * 0.15) + initial_salary
    print(f"Percentage increase: \033[34m15%\033[38m\n"
          f"Initial salary....$: \033[34m{initial_salary}\033[38m\n"
          f"Value of increase.$: \033[34m{initial_salary * 0.15}\033[38m\n"
          f"New salary........$: \033[34m{percentage_increase}\033[38m\n")

elif 700 < initial_salary <= 1500:
    percentage_increase = (initial_salary * 0.10) + initial_salary
    print(f"Percentage increase: \033[34m10%\033[38m\n"
          f"Initial salary....$: \033[34m{initial_salary}\033[38m\n"
          f"Value of increase.$: \033[34m{initial_salary * 0.10}\033[38m\n"
          f"New salary........$: \033[34m{percentage_increase}\033[38m\n")
elif initial_salary > 1500:
    percentage_increase = (initial_salary * 0.05) + initial_salary
    print(f"Percentage increase: \033[34m5%\033[38m\n"
          f"Initial salary....$:\033[34m{initial_salary}\033[38m\n"
          f"Value of increase.$: \033[34m{initial_salary * 0.05}\033[38m\n"
          f"New salary........$: \033[34m{percentage_increase}\033[38m\n")
