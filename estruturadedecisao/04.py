# https://wiki.python.org.br/EstruturaDeDecisao

vowel_or_consonant = str(input("Letter: ")).upper()

if vowel_or_consonant.isalpha() is True:
    if len(vowel_or_consonant) == 1:
        if vowel_or_consonant == 'A' or vowel_or_consonant == 'E' or vowel_or_consonant == 'I' or vowel_or_consonant ==\
                "O" or \
                vowel_or_consonant == "U":
            print(f"\033[34m{vowel_or_consonant}\033[38m is vowel!")
        else:
            print(f"\033[34m{vowel_or_consonant}\033[38m is consonant!")

    else:
        print(f"\033[34m{vowel_or_consonant}\033[38m not is a letter!")
else:
    print(f"\033[38mType just letters")
