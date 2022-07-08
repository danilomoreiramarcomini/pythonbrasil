# https://wiki.python.org.br/EstruturaDeRepeticao

number = int(input("Number: "))

for element in range(1, number + 1):

    if element > 1:

        for element_inside_element in range(2, int(element / 2) + 1):

            if (element % element_inside_element) == 0:
                break
        else:
            print(f"\033[34m{element}")
    else:
        zero = 0
