# https://wiki.python.org.br/EstruturaDeRepeticao

cd_amout = int(input("Amount cd you will buy: "))
cds_amout = []
cd_prices = []
counter = int(1)
for cd in range(1, cd_amout + 1):
    cd_price = float(input(f"{counter}º Price: "))
    cds_amout.append(1)
    cd_prices.append(cd_price)
    counter += 1

print(f"You have \033[34m{sum(cds_amout)}\033[38m cd(s). The price median for cd is $:\033[34m"
      f"{sum(cd_prices) / sum(cds_amout)}")
