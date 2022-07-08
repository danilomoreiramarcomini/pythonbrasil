# https://wiki.python.org.br/EstruturaSequencial

hours_worked = float(input("How many hours do you work per month: "))
value_per_hour = float(input("How many do you do per hour: "))
salary = hours_worked * value_per_hour
print(f"\033[38mYour salary is equal to $:\033[34m{salary:.2f}\033[38m")
