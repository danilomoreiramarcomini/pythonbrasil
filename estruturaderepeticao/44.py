# https://wiki.python.org.br/EstruturaDeRepeticao

elon_musk = int(0)
jeff_bezos = int(0)
bernard_arnault = int(0)
bill_gates = int(0)
mark_zuckerberg = int(0)
larry_page = int(0)
sergey_brin = int(0)
steve_ballmer = int(0)
warren_buffett = int(0)
null = int(0)
white = int(0)
amount = int(0)

print("VOTE IN A NEW PRESIDENT FOR WORLD\n"
      "[198] Elon Musk\n"
      "[194] Jeff Bezos\n"
      "[157] Bernard Arnault\n"
      "[149] Bill Gates\n"
      "[132] Mark Zuckerberg\n"
      "[124] Larry Page\n"
      "[119] Sergey Brin\n"
      "[105] Steve Ballmer\n"
      "[100] Warren Buffett\n"
      "[005] Null\n"
      "[006] White")
while True:
    vote = int(input("Enter with code of your candidate: "))
    amount += 1
    if vote == 198:
        elon_musk += 1
    if vote == 194:
        jeff_bezos += 1
    if vote == 157:
        bernard_arnault += 1
    if vote == 149:
        bill_gates += 1
    if vote == 132:
        mark_zuckerberg += 1
    if vote == 124:
        larry_page += 1
    if vote == 119:
        sergey_brin += 1
    if vote == 105:
        steve_ballmer += 1
    if vote == 100:
        warren_buffett += 1
    if vote == 5:
        null += 1
    if vote == 6:
        white += 1
    if vote == 0:
        print(f"Elon Musk:........\033[34m{elon_musk}\033[38m votes\n"
              f"Jeff Bezos:.......\033[34m{jeff_bezos}\033[38m votes\n"
              f"Bernard Arnault:..\033[34m{bernard_arnault}\033[38m votes\n"
              f"Bill Gates:.......\033[34m{bill_gates}\033[38m votes\n"
              f"Mark Zuckerberg:..\033[34m{mark_zuckerberg}\033[38m votes\n"
              f"Larry Page:.......\033[34m{larry_page}\033[38m votes\n"
              f"Sergey Brin:......\033[34m{sergey_brin}\033[38m votes\n"
              f"Steve Ballmer:....\033[34m{steve_ballmer}\033[38m votes\n"
              f"Warren Buffett:...\033[34m{warren_buffett}\033[38m votes")
        print(f"White votes:......\033[34m{white}\033[38m votes\n"
              f"Null votes:.......\033[34m{null}\033[38m votes\n"
              f"Null percentage:..\033[34m{(null / (amount - 1)) * 100:.0f}\033[38m %\n"
              f"White percentual:.\033[34m{(white / (amount - 1)) * 100:.0f}\033[38m %")
        break
