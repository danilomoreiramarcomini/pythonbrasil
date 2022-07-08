# https://wiki.python.org.br/EstruturaDeRepeticao

print("APU MARKET")
numbers = []
number = float(input("Product $: "))
numbers.append(number)

while True:
    number = float(input("Product $: "))
    numbers.append(number)
    if number == 0:
        print(f"Total $:\033[34m{sum(numbers)}\033[38m")
        received = float(input("Insert the number received $: "))
        if received == sum(numbers):
            print("Finished\n")
            numbers.clear()
        if received > sum(numbers):
            print(f"Your Change of money $:\033[34m{received - sum(numbers)}\033[38m")
            print("Finished\n")
            numbers.clear()
        if received < sum(numbers):
            while received < sum(numbers):
                print(f"Enter a number greater than or equal to $:\033[34m{sum(numbers)}\033[38m")
                received = float(input("Insert the number received $: "))
                if received == sum(numbers):
                    print("Finished")
                    numbers.clear()
                if received > sum(numbers):
                    print(f"Your Change of money $:\033[34m{received - sum(numbers)}\033[38m")
                    print("Finished\n")
                    numbers.clear()
