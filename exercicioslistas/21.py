# https://wiki.python.org.br/ExerciciosListas

tuple_cars = ("BMW X1", "BMW X2", "BMW X3", "BMW X4", "BMW X5")
list_km = (8.8, 7.7, 8.0, 8.6, 6.2)
price = float(2.25)
distance = float(1000)
for number in range(0, len(tuple_cars)):
    print(f"Car: \033[34m{number + 1}\033[38m\nName: \033[34m{tuple_cars[number]}\n\033[38mkilometers for liter: "
          f"\033[34m{list_km[number]}\033[38m")
print(f"\n")
print(f"Final report")

for number in range(0, len(tuple_cars)):
    print(f"\033[34m{number + 1}\033[38m - \033[34m{tuple_cars[number]}\033[38m - \033[34m{list_km[number]}\033[38m - "
          f"\033[34m{distance / list_km[number]:.0f} \033[38mliters - "
          f"$: \033[34m{(distance / list_km[number]) * price:.0f}")
