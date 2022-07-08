# https://wiki.python.org.br/EstruturaDeDecisao

input_str = str(input("Type a number between 0 and 1000: "))
input_int = int(input_str)
value_str = []

if 0 < input_int <= 9:
    value_str.append(input_str[0])
    value_str.append("0")
    value_str.append("0")
    print(f"\033[34m{input_int}\033[38m has \033[34m{value_str[0]}"
          f" units\033[38m")
if 9 < input_int <= 99:
    value_str.append(input_str[1])
    value_str.append(input_str[0])
    value_str.append("0")
    print(f"\033[34m{input_int}\033[38m has \033[34m{value_str[1]}\033[38m dozens and \033[34m{value_str[0]}"
          f" units\033[38m")
if 99 < input_int < 1000:
    value_str.append(input_str[2])
    value_str.append(input_str[1])
    value_str.append(input_str[0])
    print(f"\033[34m{input_int}\033[38m has \033[34m{value_str[2]}\033[38m hundreds, \033[34m{value_str[1]}\033[38m"
          f" dozens and \033[34m{value_str[0]}\033[38m units")
if input_int == 1000:
    print(f"\033[34m{input_int}\033[38m is equal to 1000")
if input_int > 1000:
    print(f"\033[34m{input_int}\033[38m is greater than 1000")
