# https://wiki.python.org.br/EstruturaDeRepeticao

print("Vote in a executives of group Yotsuba")
amount_people = int(input("How many people will vote: "))
counter = int(0)
reiji = []
shingo = []
kyosuke = []
while counter != amount_people:
    candidate_name = int(input("CANDIDATES\n[1] Reiji Namikawa\n[2] Shingo Mido\n[3] Kyosuke Higuchi\nDigite here: "))

    if candidate_name == 1:
        reiji.append(1)
        counter += 1
    if candidate_name == 2:
        shingo.append(1)
        counter += 1
    if candidate_name == 3:
        kyosuke.append(1)
        counter += 1
    else:
        print("Cadidate nonexistent")

if sum(reiji) > sum(shingo) and sum(reiji) > sum(kyosuke):
    print(f"\033[38mThe new president of group Yotsuba is Reiji with \033[34m{sum(reiji)}\033[38m votes Shingo with"
          f" \033[34m{sum(shingo)}\033[38m votes and Kyosuke \033[34m{sum(kyosuke)}")
if sum(shingo) > sum(reiji) and sum(shingo) > sum(kyosuke):
    print(f"\033[38mThe new president of group Yotsuba is Shingo with \033[34m{sum(shingo)}\033[38m votes Reiji with"
          f" \033[34m{sum(reiji)}\033[38m votes and Kyosuke \033[34m{sum(kyosuke)}")
if sum(kyosuke) > sum(shingo) and sum(kyosuke) > sum(reiji):
    print(f"\033[38mThe new president of group Yotsuba is Kyosuke with \033[34m{sum(kyosuke)}\033[38m votes Reiji with"
          f" \033[34m{sum(reiji)}\033[38m votes and Shingo \033[34m{sum(shingo)}")
else:
    print("\033[38mRestart the election")
