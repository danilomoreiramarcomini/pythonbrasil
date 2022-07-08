# https://wiki.python.org.br/EstruturaDeRepeticao

while True:

    deb = float(input("Enter with number of debt $: "))
    choice_form_pay = int(input("Choice the number of turn for pay the debt\n[01] [03] [06] [09] [12]\nType "
                                "here: "))
    if choice_form_pay == 1:
        fees = float(0)
        print(f"$: \033[34m{deb}\033[38m Value of installments $:\033[34m{fees}\033[38m number of installments:\033[34m"
              f"{choice_form_pay}\033[38m")
    if choice_form_pay == 3:
        fees = float(0.1)
        print(f"$: \033[34m{(deb * fees) + deb}\033[38m Value of installments $: "
              f"\033[34m{((deb * fees) + deb) / choice_form_pay:.2f}\033[38m number of installments: "
              f"\033[34m{choice_form_pay}\033[38m")
    if choice_form_pay == 6:
        fees = float(0.15)
        print(f"$: \033[34m{(deb * fees) + deb}\033[38m Value of installments $: "
              f"\033[34m{((deb * fees) + deb) / choice_form_pay:.2f}\033[38m number of installments: "
              f"\033[34m{choice_form_pay}\033[38m")
    if choice_form_pay == 9:
        fees = float(0.2)
        print(f"$: \033[34m{(deb * fees) + deb}\033[38m Value of installments $: "
              f"\033[34m{((deb * fees) + deb) / choice_form_pay:.2f}\033[38m number of installments: "
              f"\033[34m{choice_form_pay}\033[38m")
    if choice_form_pay == 12:
        fees = float(0.25)
        print(f"$: \033[34m{(deb * fees) + deb}\033[38m Value of installments $: "
              f"\033[34m{((deb * fees) + deb) / choice_form_pay:.2f} \033[38mnumber of installments:"
              f"\033[34m{choice_form_pay}\033[38m")
