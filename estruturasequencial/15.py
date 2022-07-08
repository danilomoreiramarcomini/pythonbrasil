# https://wiki.python.org.br/EstruturaSequencial

salary_per_hour = float(input("How many do you do per hour: "))
hours_worked = float(input("How many hours do you work per month: "))
gross_salary = salary_per_hour * hours_worked
income_tax = gross_salary * (15 / 100)
inss = gross_salary * (8 / 100)
syndicate = gross_salary * (5 / 100)
liquid_salary = gross_salary - (inss + income_tax + syndicate)
print(f"Gross Salary..$:\033[34m{gross_salary:.2f}\033[38m")
print(f"Income tax....$:\033[31m{income_tax:.2f}\033[38m")
print(f"INSS..........$:\033[31m{inss:.2f}\033[38m")
print(f"Syndicate.....$:\033[31m{syndicate:.2f}\033[38m")
print(f"Liquid Salary.$:\033[34m{liquid_salary:.2f}\033[38m")
