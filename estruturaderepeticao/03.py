# https://wiki.python.org.br/EstruturaDeRepeticao

old = int()
salary = float()
gender = int()
material_status = int()
name = str(input("name: ")).title()
while len(name) < 3:
    name = str(input("Name: ")).title()
old = int(input("Age: "))
while old < 0 or old > 150:
    old = int(input("Age: "))
salary = float(input("How much you make: "))
while salary <= 0:
    salary = float(input("How much you make: "))
gender = int(input("[1] Male or [2] Female: "))
while gender < 1 or gender > 2:
    gender = int(input("[1] Male or [2] Female: "))
material_status = int(input("[1] Single or [2] Maried or [3] Widower or [4] Divorced: "))
while material_status < 1 or material_status > 4:
    material_status = int(input("[1] Single or [2] Maried or [3] Widower or [4] Divorced: "))
print("\033[34mCadastre finished")
