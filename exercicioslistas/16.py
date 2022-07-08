# https://wiki.python.org.br/ExerciciosListas

import random

my_list = list()
support_list = list()
counter_list = list()
for seller in range(0, 100):
    my_list.append(round(random.uniform(0, 3000), 2))
for seller in range(0, 10):
    counter_list.append(0)
for seller in my_list:
    support_list.append(round((seller * 0.09) + (200 + seller), 2))

for seller in support_list:
    if 200 < seller <= 299:
        counter_list[0] += 1
    if 300 < seller <= 399:
        counter_list[1] += 1
    if 400 < seller <= 499:
        counter_list[2] += 1
    if 500 < seller <= 599:
        counter_list[3] += 1
    if 600 < seller <= 699:
        counter_list[4] += 1
    if 700 < seller <= 799:
        counter_list[5] += 1
    if 800 < seller <= 899:
        counter_list[6] += 1
    if 900 < seller <= 999:
        counter_list[7] += 1
    if seller >= 1000:
        counter_list[8] += 1

print(f"a. $200 - $299: \033[34m{counter_list[0]}\033[38m")
print(f"b. $300 - $399: \033[34m{counter_list[1]}\033[38m")
print(f"c. $400 - $499: \033[34m{counter_list[2]}\033[38m")
print(f"d. $500 - $599: \033[34m{counter_list[3]}\033[38m")
print(f"e. $600 - $699: \033[34m{counter_list[4]}\033[38m")
print(f"f. $700 - $799: \033[34m{counter_list[5]}\033[38m")
print(f"g. $800 - $899: \033[34m{counter_list[6]}\033[38m")
print(f"h. $900 - $999: \033[34m{counter_list[7]}\033[38m")
print(f"i. $1000  $...: \033[34m{counter_list[8]}\033[38m")
