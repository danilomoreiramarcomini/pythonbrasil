# https://wiki.python.org.br/EstruturaDeRepeticao

n_numbers = []
element_on_array = int(input("How many elements N you want add the list: "))
counter = int(0)
if element_on_array <= 0:
    print("Ok! Bye")
else:
    while True:
        number = int(input("Write a number: "))
        if number <= 0:
            print(f"{number} no is a number natural")
            break
        else:
            n_numbers.append(number)
            counter += 1
            if element_on_array == counter:
                print(f"Min: \033[34m{min(n_numbers)}\n\033[38mMax: \033[34m{max(n_numbers)}\n\033[38mSum: \033[34m"
                      f"{sum(n_numbers)}")
                break
