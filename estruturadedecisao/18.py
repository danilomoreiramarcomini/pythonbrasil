# https://wiki.python.org.br/EstruturaDeDecisao

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        maximum_number_of_days = 29
        if maximum_number_of_days >= day > 1:
            if year >= 1:
                print(f"\033[38m{day}/{month}/{year}")
            else:
                print("\033[38mInvalid date")
        else:
            print("\033[38mInvalid date")
    else:
        maximum_number_of_days = 28
        if maximum_number_of_days >= day > 1:
            if year > 1:
                print(f"\033[38m{day}/{month}/{year}")
            else:
                print("\033[38mInvalid date")
        else:
            print("\033[38mInvalid date")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    maximum_number_of_days = 31
    if maximum_number_of_days >= day > 1:
        if year > 1:
            print(f"{day}/{month}/{year}")
        else:
            print("\033[38mInvalid date")
    else:
        print("\033[38mInvalid date")

elif month == 4 or month == 6 or month == 9 or month == 11:
    maximum_number_of_days = 30
    if maximum_number_of_days >= day > 1:
        if year > 1:
            print(f"\033[38m{day}/{month}/{year}")
        else:
            print("\033[38mInvalid date")
    else:
        print("\033[38mInvalid date")

elif month < 1 or month > 12:
    print("\033[38mInvalid date")
