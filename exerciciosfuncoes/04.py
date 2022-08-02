def checking_number(number):
    if number > 0:
        return "Positive"
    else:
        return "Negative"


print(checking_number(float(input("Number: "))))
