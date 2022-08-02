def show_n(n_integer):
    for number in range(1, n_integer + 1):
        print(f"{number} " * number)


show_n(int(input("Number: ")))
