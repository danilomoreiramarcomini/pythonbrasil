# https://wiki.python.org.br/EstruturaDeDecisao

a = float(input("Enter with number of a: "))
if a == 0:
    print(f"'a' cannot be 0")

if a != 0:
    b = float(input("Enter with number of b: "))
    c = float(input("Enter with number of player: "))
    delta = (b ** 2 - 4 * a * c)
    value_ax = (-b + delta ** (1 / 2)) / (2 * a)
    value_bx = (-b - delta ** (1 / 2)) / (2 * a)

    if delta <= 0:
        print(f"Only real roots")
    if delta > 0:
        print(f"\033[38mThe root of the first X equal \033[34m{value_ax}\033[38m the root of the second X is equal \033"
              f"[34m{value_bx}\033[38m")
