# https://wiki.python.org.br/EstruturaDeRepeticao

number = int(input("Type a number in between 0 and 10: "))
while True:
    if number < 0 or number > 10:
        number = int(input("type a number in between: "))
    else:
        print(f"\033[38mYou writed \033[34m{number}")
        break
