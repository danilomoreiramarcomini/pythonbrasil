# https://wiki.python.org.br/EstruturaDeDecisao

hours_worked = float(input("Your number per hour worked: "))
hour_in_month = float(input("How many hours do you work per month: "))
salary = float(hour_in_month * hours_worked)

if salary <= 900:
    income_tax = str("Free")
    inss = (salary * 0.10)
    fgts = (salary * 0.11)
    total_discounts = (inss + fgts)
    liquid_salary = salary - total_discounts
    print(f"Gross salary..........$:\033[34m{hours_worked * hour_in_month}\033[38m\n"
          f"(-) Income tax (5%)...$:\033[34m{income_tax}\033[38m\n"
          f"(-) INSS (10%)........$:\033[34m{inss}\033[38m\n"
          f"FGTS (11%)............$:\033[34m{fgts}\033[38m\n"
          f"Total discounts.......$:\033[34m{total_discounts}\033[38m\n"
          f"Liquid salary.........$:\033[34m{liquid_salary}\033[38m")

elif 900 < salary <= 1500:
    income_tax = (salary * 0.05)
    inss = (salary * 0.10)
    fgts = (salary * 0.11)
    total_discounts = (income_tax + inss + fgts)
    liquid_salary = salary - total_discounts
    print(f"Gross salary..........$:\033[34m{hours_worked * hour_in_month}\033[38m\n"
          f"(-) Income tax (5%)...$:\033[34m{income_tax}\033[38m\n"
          f"(-) INSS (10%)........$:\033[34m{inss}\033[38m\n"
          f"FGTS (11%)............$:\033[34m{fgts}\033[38m\n"
          f"Total discounts.......$:\033[34m{total_discounts}\033[38m\n"
          f"Liquid salary.........$:\033[34m{liquid_salary}\033[38m")

elif 1500 < salary <= 2500:
    income_tax = (salary * 0.10)
    inss = (salary * 0.10)
    fgts = (salary * 0.11)
    total_discounts = (income_tax + inss + fgts)
    liquid_salary = salary - total_discounts
    print(f"Gross salary..........$:\033[34m{hours_worked * hour_in_month}\033[38m\n"
          f"(-) Income tax (5%)...$:\033[34m{income_tax}\033[38m\n"
          f"(-) INSS (10%)........$:\033[34m{inss}\033[38m\n"
          f"FGTS (11%)............$:\033[34m{fgts}\033[38m\n"
          f"Total discounts.......$:\033[34m{total_discounts}\033[38m\n"
          f"Liquid salary.........$:\033[34m{liquid_salary}\033[38m")

elif salary > 2500:
    income_tax = (salary * 0.20)
    inss = (salary * 0.10)
    fgts = (salary * 0.11)
    total_discounts = (income_tax + inss + fgts)
    liquid_salary = salary - total_discounts
    print(f"Gross salary..........$:\033[34m{hours_worked * hour_in_month}\033[38m\n"
          f"(-) Income tax (5%)...$:\033[34m{income_tax}\033[38m\n"
          f"(-) INSS (10%)........$:\033[34m{inss}\033[38m\n"
          f"FGTS (11%)............$:\033[34m{fgts}\033[38m\n"
          f"Total discounts.......$:\033[34m{total_discounts}\033[38m\n"
          f"Liquid salary.........$:\033[34m{liquid_salary}\033[38m")
