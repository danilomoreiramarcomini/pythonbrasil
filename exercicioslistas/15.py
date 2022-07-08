# https://wiki.python.org.br/ExerciciosListas

list_notes = list()

while True:
    note = float(input("Enter with a note: "))
    if note != -1:
        list_notes.append(note)
    if note == -1:
        break


print(f"You typed \033[34m{len(list_notes)}\033[38m")

for number in list_notes:
    print(f"\033[34m{number}\033[38m", end=" ")
print("\n")

list_notes.sort(reverse=True)
for number in list_notes:
    print(f"\033[34m{number}\033[38m")

print("\n")
print(f"The sum:\033[34m{sum(list_notes)}")
print("\n")
average = float(sum(list_notes) / len(list_notes))
print(f"\033[38mThe average:\033[34m{average:.2f}")
print(f"\033[38mThe numbers above average:\033[34m")
for number in list_notes:
    if number > average:
        print(f"\033[34m{number}\033[38m")
print(f"The numbers above 7: ")
for number in list_notes:
    if number < 7:
        print(f"\033[34m{number}\033[38m")

print(f"Bye")
