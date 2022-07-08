# https://wiki.python.org.br/EstruturaDeRepeticao

jumps = []
while True:
    name_athlete = str(input("Athlete Name: ")).title()
    if name_athlete == " ":
        break
    else:
        for jump in range(1, 6):
            distance_jump = float(input(f"\033[34m{jump}\033[38mº jump: "))
            jumps.append(distance_jump)
        max_jump = max(jumps)
        min_jump = min(jumps)
        print(f"The better jump:\033[34m{max_jump}\033[38m metters \nThe worse jump:\033[34m{min_jump}\033[38m metters")
        jumps.remove(max_jump)
        jumps.remove(min_jump)

        print(f"The average of others jumps:\033[34m{(sum(jumps) / len(jumps)):.1f}\033[38m meters")
        jumps.clear()
