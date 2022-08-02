def sum_tax(tax, cots):
    return f"$: {((tax / 100) * cots) + cots}"


print(sum_tax(float(input("Tax: ")), float(input("Cots: "))))
