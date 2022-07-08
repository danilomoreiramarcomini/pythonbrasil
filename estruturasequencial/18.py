# https://wiki.python.org.br/EstruturaSequencial

link_speed = float(input("Type the link speed: "))
size_of_file = float(input("Type the size of file: "))
link_speed_per_megabits = float(link_speed / 8)
time_to_download = size_of_file / link_speed_per_megabits

print(f"\033[38mTime to download \033[34m{time_to_download:.2f}\033[38m minutes")
