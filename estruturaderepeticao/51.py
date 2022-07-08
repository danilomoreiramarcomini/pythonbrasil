# https://wiki.python.org.br/EstruturaDeRepeticao

ns = []
ms = []
terms = []
n_by_input = int(input("Enter with N term: "))
m_by_input = int(input("Enter with M term: "))

if n_by_input < m_by_input:
    for n in range(1, n_by_input, 1):
        ns.append(n)
    for m in range(1, m_by_input, 2):
        ms.append(m)

    for number in range(0, len(ns)):
        print(f"{ns[number]}/{ms[number]}")
        if ms[number] == ms[-1]:
            break
        else:
            terms.append(ns[number] / ms[number])

    print(f"The sum of series of terms is \033[34m{sum(terms):.2f}\033[38m")
else:
    print("\033[34mM\033[38m can't be bigger what \033[34mN\033[38m")
