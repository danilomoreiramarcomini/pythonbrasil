# https://wiki.python.org.br/EstruturaDeDecisao

first_side = float(input("Sides of the triangle: "))
second_side = float(input("Sides of the triangle: "))
third_side = float(input("Sides of the triangle: "))

if first_side + second_side > third_side and first_side + third_side > second_side and second_side + \
        third_side > first_side:
    if first_side == second_side == third_side:
        print("\033[34mEquilateral triangle\033[38m")
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        print("\033[34mIsosceles triangle\033[38m")
    elif first_side != second_side != third_side:
        print("\033[34mScalene triangle\033[38m")
else:
    print("\033[31mInvalid dictionary\033[38m")
