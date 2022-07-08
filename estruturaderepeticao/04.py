# https://wiki.python.org.br/EstruturaDeRepeticao

a = 80000
b = 200000
counter = 0
while a < b:
    a = a + (a * 0.03)
    b = b + (b * (0.01 + (0.01 / 2)))
    counter += 1
print(f"The A population need \033[34m{counter}\033[38m years for to surpass the population B")
