# https://wiki.python.org.br/ExerciciosListas

list_quest = list()

called = int(input("Called the victim? [1 Yes or 2 No]: "))
place = int(input("Been at the place ? [1 Yes or 2 No]: "))
live = int(input("Live near ? [1 Yes or 2 No]: "))
should = int(input("Should the victim ? [1 Yes or 2 No]: "))
work = int(input("Work with victim? ? [1 Yes or 2 No]: "))

if called == 1:
    list_quest.append(called)
if place == 1:
    list_quest.append(place)
if live == 1:
    list_quest.append(live)
if should == 1:
    list_quest.append(should)
if work == 1:
    list_quest.append(work)

if len(list_quest) == 5:
    print("\033[34mKiller")
elif len(list_quest) == 4:
    print("\033[34mAccomplice")
elif len(list_quest) == 3:
    print("\033[34mAccomplice")
elif len(list_quest) == 2:
    print("\033[34mSuspect")
elif len(list_quest) == 1:
    print("\033[34mInnocent")
else:
    print("\033[34mInnocent")
