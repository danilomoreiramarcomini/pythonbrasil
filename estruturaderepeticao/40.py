# https://wiki.python.org.br/EstruturaDeRepeticao

from statistics import median

town_code = []
passenger_vehicles = []
passenger_vehicles_copy = []
victims = []
victims_copy = []
support = list()
while len(town_code) != 5:
    town_code_by_input = int(input("Enter with the town code: "))
    town_code.append(town_code_by_input)
    passenger_vehicles_by_input = int(input("Enter with the number of passenger vehicles: "))
    passenger_vehicles.append(passenger_vehicles_by_input)
    number_of_victims = int(input("Enter with number of victims: "))
    print('-' * 30)
    victims.append(number_of_victims)

max_victims = max(victims)
min_victims = min(victims)
max_victims_position = victims.index(max_victims)
min_victims_position = victims.index(min_victims)

print(f"The town with code \033[34m{town_code[max_victims_position]}\033[38m has the highest index of victims "
      f"with \033[34m{max_victims}\033[38m death for year")
print(f"The town with code \033[34m{town_code[min_victims_position]}\033[38m has the lowest index of victims "
      f"with \033[34m{min_victims}\033[38m death for year")

for town in passenger_vehicles:
    if town >= 2000:
        support.append(town)

average_passenger_vehicles = float(sum(support)/len(support))
print(f"The average of passenger Vehicles in all towns is with more passenger vehicles is\033[34m {median(support):.0f}"
      f"\033[38m")
