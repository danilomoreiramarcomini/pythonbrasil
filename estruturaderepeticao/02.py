# https://wiki.python.org.br/EstruturaDeRepeticao

name = str(input("Name: ")).title()
password = str(input("Passaword: ")).title()
while True:
    if name == password:
        print("Name and password equals. Change your password")
        name = str(input("Name: ")).title()
        password = str(input("Passawor: ")).title()
    else:
        print(f"Welcome, \033[34m{name}\033[38m!")
        break
