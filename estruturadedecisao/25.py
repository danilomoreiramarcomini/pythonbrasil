# https://wiki.python.org.br/EstruturaDeDecisao

yes = "Yes"
print("Type Yes or No")
a = str(input("You called to victim: ")).title()
b = str(input("Was in location of crime: ")).title()
c = str(input("Lived near of victim: ")).title()
d = str(input("Owed money to victim: ")).title()
e = str(input("You worked with a victim: ")).title()

if a == yes and b == yes and c == yes and d == yes and e == yes:
    print("\033[34mGuilty")

elif a == yes and b == yes and c == yes and d == yes or a == yes and b == yes and c == yes and e == yes\
        or a == yes and b == yes and d == yes and e == yes or a == yes and c == yes and d == yes and e ==\
        yes or b == yes and c == yes and d == yes and e == yes or a == yes and b == yes and c == yes or\
        a == yes and b == yes and d == yes or a == yes and b == yes \
        and e == yes or c == yes and a == yes and d == yes or c == yes and a == yes \
        and e == yes or d == yes and a == yes and e == yes or d == yes and c == yes \
        and e == yes or e == yes and b == yes and c == yes or b == yes and c == yes and d == yes:
    print("\033[34mAccomplice")

elif a == yes and b == yes or a == yes and c == yes or a == yes and d == yes or a == yes and e == yes \
        or b == yes and c == yes or b == yes and d == yes or b == yes and e == yes or c == yes and d == \
        yes or c == yes and e == yes or d == yes:
    print("\033[34mSuspect")

else:
    print("\033[34mInnocent")
