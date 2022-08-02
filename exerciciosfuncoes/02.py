def show_n(n_integer):
    numbers = list()
    for i in range(1, n_integer):
        numbers.append(str(i))
        print(" ".join(numbers))


show_n(int(input("Number: ")))
