# https://wiki.python.org.br/EstruturaSequencial

area = float(input("Type the size in square meters: "))
liter = (area / 6)
cans = (liter/18)
cans_round = round(liter/18)
gallons_round = round(liter/3.6)
leftover_paints = cans % cans_round
leftover_paints_gallons = round(leftover_paints + (leftover_paints + (leftover_paints * 0.10)) / 3.6)

print(f"• Buy {cans_round} ink cans")
print(f"• Buy {gallons_round} ink gallons")
print(f"• Buy {cans_round} ink cans and {leftover_paints_gallons} inkl gallons")
