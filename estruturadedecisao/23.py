# https://wiki.python.org.br/EstruturaDeDecisao

number = float(input("Type a number: "))

if number // 1 == number:
    print("\033[38mInteger")
else:
    print("\033[38mDecimal")
