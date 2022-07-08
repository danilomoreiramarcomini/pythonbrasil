# https://wiki.python.org.br/EstruturaDeDecisao

year = int(input("Type the year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("\033[38mLeap year")
else:
    print(f"\033[38mCommon year")
