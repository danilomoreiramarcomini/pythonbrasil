# https://wiki.python.org.br/EstruturaDeDecisao

first_number = str(input("First number: "))
second_number = str(input("Second number: "))
result_of_input = int(input("[1] Add numbers \n"
                            "[2] Multiply numbers\n"
                            "[3] Subtract numbers\n"
                            "[4] Divide numbers\n"
                            "Write here:"))

if result_of_input == 1:
    result_float = float(first_number) + float(second_number)
    result_int = result_float // 1
    print(f"The sum between numbers is \033[34m{result_float:.1f}")
    if result_float % 2 == 0:
        print("\033[38ma. \033[34mEven")
    if result_float % 2 != 0:
        print("\033[38ma. \033[34mOdd")
    if result_float >= 0:
        print("\033[38mb. \033[34mPositive")
    if result_float < 0:
        print("\033[38mb. \033[34mNegative")
    if result_float == result_int:
        print("\033[38mc. \033[34mInteger")
    if result_float != result_int:
        print("\033[38mc. \033[34mDecimal")
if result_of_input == 2:
    result_float = float(first_number) * float(second_number)
    result_int = result_float // 1
    print(f"\033[38mThe sum between numbers is \033[34m{result_float:.1f}")
    if result_float % 2 == 0:
        print("\033[38ma. \033[34mEven")
    if result_float % 2 != 0:
        print("\033[38ma. \033[34mOdd")
    if result_float >= 0:
        print("\033[38mb. \033[34mPositive")
    if result_float < 0:
        print("\033[38mb. \033[34mNegative")
    if result_float == result_int:
        print("\033[38mc. \033[34mInteger")
    if result_float != result_int:
        print("\033[38mc. \033[34mDecimal")
if result_of_input == 3:
    result_float = float(first_number) - float(second_number)
    result_int = result_float // 1
    print(f"\033[38mThe sum between numbers is \033[34m{result_float:.1f}")
    if result_float % 2 == 0:
        print("\033[38ma. \033[34mEven")
    if result_float % 2 != 0:
        print("\033[38ma. \033[34mOdd")
    if result_float >= 0:
        print("\033[38mb. \033[34mPositive")
    if result_float < 0:
        print("\033[38mb. \033[34mNegative")
    if result_float == result_int:
        print("\033[38mc. \033[34mInteger")
    if result_float != result_int:
        print("\033[38mc. \033[34mDecimal")
if result_of_input == 4:
    if second_number == 0:
        print("\033[34mNot divide by zero")
    else:
        result_float = float(first_number) / float(second_number)
        result_int = result_float // 1
        print(f"\033[38mThe sum between numbers is \033[34m{result_float:.1f}")
        if result_float % 2 == 0:
            print("\033[38ma. \033[34mEven")
        if result_float % 2 != 0:
            print("\033[38ma. \033[34mOdd")
        if result_float >= 0:
            print("\033[38mb. \033[34mPositive")
        if result_float < 0:
            print("\033[38mb. \033[34mNegative")
        if result_float == result_int:
            print("\033[38mc. \033[34mInteger")
        if result_float != result_int:
            print("\033[38mc. \033[34mDecimal")
