# https://wiki.python.org.br/EstruturaDeRepeticao

import statistics

temperature = int(input("How many dictionary do you want to insert: "))
temperatures = []
temperature_str = float(input("Enter the temperature in celsius Cº: "))
temperatures.append(temperature_str)
while len(temperatures) != temperature:
    temperature_str = float(input("Enter the temperature in celsius Cº: "))
    temperatures.append(temperature_str)
    if len(temperatures) == temperature:
        print(f"The median of temperature is \033[34m{statistics.median(temperatures)}\033[38m ºC")
        print(f"The Max is \033[34m{max(temperatures)}\033[38m ºC")
        print(f"The Min is \033[34m{min(temperatures)}\033[38m ºC")
