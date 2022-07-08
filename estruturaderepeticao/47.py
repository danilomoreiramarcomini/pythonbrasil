# https://wiki.python.org.br/EstruturaDeRepeticao

notes = []
while True:
    gymnast_name = str(input("Gymnast name: ")).title()
    for note in range(1, 8):
        note_by_input = float(input(f"Enter with \033[34m{note}\033[38mº note: "))
        notes.append(note_by_input)
    max_note = max(notes)
    min_note = min(notes)
    print(f"Athlete:\033[34m{gymnast_name}\033[38m")
    for n in notes:
        print(f"Note:\033[34m{n}\033[38m")
    print(f"Result finale:\nAthleta:\033[34m{gymnast_name}\033[38m\nBetter note:\033[34m{max(notes)}\033[38m\n"
          f"Worse note:\033[34m{min(notes)}\033[38m")
    notes.remove(max_note)
    notes.remove(min_note)
    print(f"\033[38mThe average:\033[34m{(sum(notes) / len(notes)):.2f}\033[38m")
