# https://wiki.python.org.br/EstruturaDeDecisao

sex_verification = str(input("TGender: ")).upper()

if sex_verification == "M":
    print("Male Gender")
elif sex_verification == "F":
    print("Female Gender")
else:
    print("\033[31mCRITICAL ERROR\033[38m")
