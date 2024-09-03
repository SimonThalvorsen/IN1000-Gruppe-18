konto = "1234.1234.1234.1234"
saldo = 1000

def sett_inn():
    global saldo
    gammel = saldo
    saldo += int(input("Hvor mye vil du sette inn?\n>"))
    print(f"Ny saldo: {saldo}")

def sjekk_saldo():
    print(f"Kontonr. {konto}")
    print("Saldo:", saldo)

def ta_ut():
    global saldo
    # sjekk_saldo()
    gammel = saldo
    saldo -= int(input("Hvor mye vil du ta ut?\n>"))
    print(f"Ny saldo: {saldo}")

def meny():
    print("Velkommen til ABC-bank! \n\
Tast:\n\
    1 - For å sjekke saldo,\n\
    2 - For uttak,\n\
    3 - For innskudd, \n")
    inp = input(">")
    if inp == "1":
        sjekk_saldo()

    elif inp == "2":
        ta_ut()
    elif inp == "3":
        sett_inn()
    else:
        print("Ukjent kommando\n")

meny()
