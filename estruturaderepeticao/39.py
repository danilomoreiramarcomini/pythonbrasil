# https://wiki.python.org.br/EstruturaDeRepeticao

group_of_arrays = [[], [], [], [], [], [], [], [], [], []]
new_group_of_arrays = []
counter = int(0)
count_group_array = len(group_of_arrays)
for item in range(0, count_group_array):
    id_student = int(input("Insert the ID of student: "))
    group_of_arrays[item].insert(0, id_student)
    height_student = int(input("Enter student height in centimeters: "))
    group_of_arrays[item].insert(1, height_student)
    new_group_of_arrays.append(group_of_arrays[item][1])
    group_of_arrays[item].pop(1)
    max_height = max(new_group_of_arrays)
    max_height_position = new_group_of_arrays.index(max_height)
    min_height = min(new_group_of_arrays)
    min_height_position = new_group_of_arrays.index(min_height)
    id_max_position = group_of_arrays[max_height_position]
    id_min_position = group_of_arrays[min_height_position]
    counter += 1
    if counter == count_group_array:
        print(f"The higher student has \033[34m{max_height}\033[38m cm and your ID is: \033[34m{id_max_position[0]}"
              f"\033[38m")
        print(f"The lower student has \033[34m{min_height}\033[38m cm and your ID is: \033[34m{id_min_position[0]}"
              f"\033[38m")
