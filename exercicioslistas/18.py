# https://wiki.python.org.br/ExerciciosListas

players_list = list()
for player in range(0, 23):
    players_list.append(0)

while True:
    vote = int(input("Number of the player:"))

    if 1 == vote:
        players_list[0] += 1
    if 2 == vote:
        players_list[1] += 1
    if 3 == vote:
        players_list[2] += 1
    if 4 == vote:
        players_list[3] += 1
    if 5 == vote:
        players_list[4] += 1
    if 6 == vote:
        players_list[5] += 1
    if 7 == vote:
        players_list[6] += 1
    if 8 == vote:
        players_list[7] += 1
    if 9 == vote:
        players_list[8] += 1
    if 10 == vote:
        players_list[9] += 1
    if 11 == vote:
        players_list[10] += 1
    if 12 == vote:
        players_list[11] += 1
    if 13 == vote:
        players_list[12] += 1
    if 14 == vote:
        players_list[13] += 1
    if 15 == vote:
        players_list[14] += 1
    if 16 == vote:
        players_list[15] += 1
    if 17 == vote:
        players_list[16] += 1
    if 18 == vote:
        players_list[17] += 1
    if 19 == vote:
        players_list[18] += 1
    if 20 == vote:
        players_list[19] += 1
    if 21 == vote:
        players_list[20] += 1
    if 22 == vote:
        players_list[21] += 1
    if 23 == vote:
        players_list[22] += 1
    if vote == 0:
        break

print(f"Result of voting: ")
print(f"Total of vote: \033[34m{sum(players_list)}\033[38m")
print(f"\n")
print(f"Players - Votes - %")

for player in players_list:
    if player > 0:
        number_of_player = int(players_list.index(player) + 1)
        amount_votes = int(player)
        percentage_of_votes = float(100 / (sum(players_list) / player))
        print(f"\033[34m{number_of_player}\033[38m - \033[34m{amount_votes}\033[38m - \033[34m{percentage_of_votes:.0f}"
              f"\033[38m%")
