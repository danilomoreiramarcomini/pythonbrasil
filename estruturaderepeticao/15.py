# https://wiki.python.org.br/EstruturaDeRepeticao

nth_term = int(input("Insert the nth term: "))
first_support = int(0)
second_support = int(1)
third_support = int(0)
counter = int(3)
print(f"\033[34m{second_support}", end=' ')
while counter <= nth_term:
    third_support = first_support + second_support
    first_support = second_support
    second_support = third_support
    counter += 1
    print(f"\033[34m{third_support}", end=' ')
