# https://wiki.python.org.br/EstruturaDeDecisao

print("[1] - Sunday [2] - Monday [3] - Tuesday [4] - Wednesday [5] - Thursday [6] - Friday [7] - Saturday")
day = str(input("Number: "))

if day.isnumeric() is True:
    if day == "7":
        day_of_the_week = "Saturday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day == "6":
        day_of_the_week = "Friday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day == "5":
        day_of_the_week = "Thursday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day == "4":
        day_of_the_week = "Wednesday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day == "3":
        day_of_the_week = "Tuesday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day == "2":
        day_of_the_week = "Monday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day == "1":
        day_of_the_week = "Sunday"
        print(f"Day: \033[34m{day_of_the_week}\033[38m")
    elif day < "1" or day > "7":
        print(f"\033[31mInvalid\033[38m")
else:
    print(f"\033[31mInvalid\033[38m")
