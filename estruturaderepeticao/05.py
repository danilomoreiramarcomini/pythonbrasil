# https://wiki.python.org.br/EstruturaDeRepeticao

a = int(input("Enter with the number of population A: "))
b = int(input("Enter with the number of population B: "))
growth_rate_a = float(input("Enter with the number of growth rate: "))
growth_rate_b = float(input("Enter with the number of growth rate: "))

counter = 0
while a < b:
    a = a + (a * (growth_rate_a / 100))
    b = b + (b * (growth_rate_b / 100))
    counter += 1
print(f"The \033[34mA\033[38m population need \033[34m{counter}\033[38m years for to surpass the population \033[34mB"
      f"\033[38m")
