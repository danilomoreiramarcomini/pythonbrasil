# https://wiki.python.org.br/EstruturaDeRepeticao

odd = []
pair = []
for number in range(1, 11, 1):
    number_by_input = int(input("Insert a number: "))
    if number_by_input % 2 == 0:
        pair.append(number_by_input)
    else:
        odd.append(number_by_input)
print(f"\033[38mODDS: ")
for element in odd:
    print(f"\033[34m{element}", end=' ')


print(f"\n\033[38mPAIRS: ")
for element in pair:
    print(f"\033[34m{element}", end=' ')
