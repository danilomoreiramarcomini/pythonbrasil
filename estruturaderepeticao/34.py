# https://wiki.python.org.br/EstruturaDeRepeticao

while True:
    number = int(input("Number: "))

    if number > 1:

        for element in range(2, int(number / 2) + 1):

            if (number % element) == 0:
                print(f"\033[34m{False}\033[38m")
                break
        else:
            print(f"\033[34m{True}\033[38m")
    else:
        print(f"\033[34m{False}\033[38m")
