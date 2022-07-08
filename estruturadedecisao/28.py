# https://wiki.python.org.br/EstruturaDeDecisao

mean = int(input("[1] Double Filet\n[2] Rump Cap\n[3] Rump Cover\nWrite here: "))
if mean == 1:
    amount_meat = float(input("Write the amount meat: "))
    if amount_meat <= 5:
        value_meat = 4.9
        choice_pay = int(input("[1] Money\n[2] Card\nWrite here: "))
        if choice_pay == 1:
            total_price = amount_meat * value_meat
            print(f"Type of Meat:.Doulbe Filet\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price...$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mMoney\033[38m\n"
                  f"Discont:......$:\033[34m00.00\033[38m\n"
                  f"Buy Price.....$:\033[34m{total_price:.2f}\033[38m")
        elif choice_pay == 2:
            total_price = amount_meat * value_meat
            discont = (total_price * 0.05)
            new_total_price = total_price - discont
            print(f"Type of Meat:.Doulbe Filet\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price:..$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mCard\033[38m\n"
                  f"Discont:......$:\033[34m{discont:.2f}\033[38m\n"
                  f"Buy Price.....$:\033[34m{new_total_price:.2f}\033[38m")

    else:
        value_meat = 5.8
        choice_pay = int(input("[1] Money\n[2] Card\nWrite here: "))
        if choice_pay == 1:
            total_price = amount_meat * value_meat
            print(f"Type of Meat:.Doulbe Filet\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price...$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mMoney\033[38m\n"
                  f"Discont:......$:\033[34m00.00\033[38m\n"
                  f"Buy Price.....$:\033[34m{total_price:.2f}\033[38m")
        elif choice_pay == 2:
            total_price = amount_meat * value_meat
            discont = (total_price * 0.05)
            new_total_price = total_price - discont
            print(f"Type of Meat:.Doulbe Filet\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price:..$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mCard\n\033[38m"
                  f"Discont:......$:\033[34m{discont:.2f}\n\033[38m"
                  f"Buy Price.....$:\033[34m{new_total_price:.2f}m\033[38m")
if mean == 2:
    amount_meat = float(input("Write the amount meat: "))
    if amount_meat <= 5:
        value_meat = 5.9
        choice_pay = int(input("[1] Money\n[2] Card\nWrite here: "))
        if choice_pay == 1:
            total_price = amount_meat * value_meat
            print(f"Type of Meat:.Rump Cap\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price...$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mMoney\033[38m\n"
                  f"Discont:......$:\033[34m00.00\033[38m\n"
                  f"Buy Price.....$:\033[34m{total_price:.2f}\033[38m")
        elif choice_pay == 2:
            total_price = amount_meat * value_meat
            discont = (total_price * 0.05)
            new_total_price = total_price - discont
            print(f"Type of Meat:.Rump Cap\n"
                  f"Amount:.......:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price:.$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:..:\033[34mCard\033[38m\n"
                  f"Discont: $:...:\033[34m{discont:.2f}\033[38m\n"
                  f"Buy Price $:..:\033[34m{new_total_price:.2f}\033[38m")

    else:
        value_meat = 6.8
        choice_pay = int(input("[1] Money\n[2] Card\nWrite here: "))
        if choice_pay == 1:
            total_price = amount_meat * value_meat
            print(f"Type of Meat:.Rump Cap\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price...$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mMoney\033[38m\n"
                  f"Discont.......$:\033[34m00.00\033[38m\n"
                  f"Buy Price.....$:\033[34m{total_price:.2f}\033[38m")
        elif choice_pay == 2:
            total_price = amount_meat * value_meat
            discont = (total_price * 0.05)
            new_total_price = total_price - discont
            print(f"Type of Meat:.Rump Cap\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price:..$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mCard\033[38m\n"
                  f"Discont.......$:\033[34m{discont:.2f}\033[38m\n"
                  f"Buy Price.....$:\033[34m{new_total_price:.2f}\033[38m")
if mean == 3:
    amount_meat = float(input("Write the amount meat: "))
    if amount_meat <= 5:
        value_meat = 6.9
        choice_pay = int(input("[1] Money\n[2] Card\nWrite here: "))
        if choice_pay == 1:
            total_price = amount_meat * value_meat
            print(f"Type of Meat:.Rump Cover\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price...$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mMoney\033[38m\n"
                  f"Discont:......$:\033[34m00.00\033[38m\n"
                  f"Buy Price.....$:\033[34m{total_price:.2f}\033[38m")
        elif choice_pay == 2:
            total_price = amount_meat * value_meat
            discont = (total_price * 0.05)
            new_total_price = total_price - discont
            print(f"Type of Meat:.Rump Cover\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price:..$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mCard\n\033[38m"
                  f"Discont:......$:\033[34m{discont:.2f}\n\033[38m"
                  f"Buy Price.....$:\033[34m{new_total_price:.2f}\033[38m")

    else:
        value_meat = 7.8
        choice_pay = int(input("[1] Money\n[2] Card\nWrite here: "))
        if choice_pay == 1:
            total_price = amount_meat * value_meat
            print(f"Type of Meat:.Rump Cover\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price...$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mMoney\033[38m\n"
                  f"Discont:......$:\033[34m00.00\033[38m\n"
                  f"Buy Price.....$:\033[34m{total_price:.2f}\033[38m")
        elif choice_pay == 2:
            total_price = amount_meat * value_meat
            discont = (total_price * 0.05)
            new_total_price = total_price - discont
            print(f"Type of Meat:.Rump Cover\n"
                  f"Amount:........:\033[34m{amount_meat}\033[38m kilogram\n"
                  f"Total Price:..$:\033[34m{total_price:.2f}\033[38m\n"
                  f"Type of Pay:...:\033[34mCard\033[38m\n"
                  f"Discont:......$:\033[34m{discont:.2f}\033[38m\n"
                  f"Buy Price.....$:\033[34m{new_total_price:.2f}\033[38m")
