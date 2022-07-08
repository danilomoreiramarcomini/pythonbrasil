# https://wiki.python.org.br/EstruturaDeDecisao

amount_withdrawn = int(input("How much do you want to withdraw: "))
one_hundred_dollars = (amount_withdrawn // 100)
fifty_dollars = (amount_withdrawn % 100) // 50
ten_dollars = ((amount_withdrawn % 100) % 50) // 10
five_dollars = (((amount_withdrawn % 100) % 50) % 10) // 5
one_dollar = ((((amount_withdrawn % 100) % 50) % 10) % 5)

if 10 <= amount_withdrawn <= 600:
    if one_hundred_dollars != 0:
        print(f"\033[38mwithdraw \033[34m{one_hundred_dollars} \033[38mnotes of $:\033[34m100.00")
    if fifty_dollars != 0:
        print(f"\033[38mwithdraw \033[34m{fifty_dollars} \033[38mnotes of $:\033[34m50.00")
    if ten_dollars != 0:
        print(f"\033[38mwithdraw \033[34m{ten_dollars} \033[38mnotes of $:\033[34m10.00")
    if five_dollars != 0:
        print(f"\033[38mwithdraw \033[34m{five_dollars} \033[38mnotes of $:\033[34m5.00")
    if one_dollar != 0:
        print(f"\033[38mwithdraw \033[34m{one_dollar} \033[38mnotes of $:\033[34m1.00")
else:
    print(f"\033[38mWithdraw more than $:10.00 and less than $:\033[34m600.00")
