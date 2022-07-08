# https://wiki.python.org.br/EstruturaDeRepeticao

from statistics import median

ids = []
weights = []
heights = []

id_by_input = int(input("Enter with your ID: "))
ids.append(id_by_input)
weight = float(input("Enter with your weigth: "))
weights.append(weight)
height = float(input("Enter with your height: "))
heights.append(height)

while id_by_input != 0:
    id_by_input = int(input("Enter with your ID: "))
    ids.append(id_by_input)
    if id_by_input == 0:
        max_weight = max(weights)
        min_weight = min(weights)
        max_weight_position = weights.index(max_weight)
        min_weight_position = weights.index(min_weight)
        max_height = max(heights)
        min_height = min(heights)
        maxHeightPosition = heights.index(max_height)
        minHeightPosition = heights.index(min_height)

        print(f"The heaviest customer has \033[34m{max_weight:.2f}\033[38m Kg your id is \033[34m"
              f"{ids[max_weight_position]}\033[38m")
        print(f"The lightest customer has \033[34m{min_weight:.2f}\033[38m Kg your id is \033[34m"
              f"{ids[min_weight_position]}\033[38m")
        print(f"The highest customer has \033[34m{max_height:.2f}\033[38m Cm your id is \033[34m"
              f"{ids[maxHeightPosition]}\033[38m")
        print(f"The smallest customer has \033[34m{min_height:.2f}\033[38m Cm your id is \033[34m"
              f"{ids[minHeightPosition]}\033[38m")
        print(f"The median of weight is \033[34m{median(weights):.2f}\033[38m kiloram")
        print(f"The median of height is \033[34m{median(heights):.2f}\033[38m centimeters")

        break
    weight = float(input("Enter with your weigth: "))
    weights.append(weight)
    height = float(input("Enter with your height: "))
    heights.append(height)
