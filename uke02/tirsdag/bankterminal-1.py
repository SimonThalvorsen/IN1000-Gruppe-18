konto = "1234.1234.1234.1234"
saldo = 1000

def sett_inn():
    global saldo
    gammel = saldo
    saldo += int(input("Hvor mye vil du sette inn?\n>"))
    print(f"Ny saldo: {saldo}\nGammel saldo:{gammel}")

def sjekk_saldo():
    print(f"Kontonr. {konto}")
    print("Saldo:", saldo)

def ta_ut():
    global saldo
    sjekk_saldo()
    gammel = saldo
    inp = int(input("Hvor mye vil du ta ut?\n>"))
    if inp > saldo:
        print("Du har ikke nok penger på konto!")
        print(f"Saldo: {gammel}")
        print(f"Forsøkt uttak: {inp}")
    else:
        saldo -= inp
        print(f"Ny saldo: {saldo}\nGammel saldo:{gammel}")

def kommandoer():
    print("Velkommen til ABC-bank! \n\
    Tast:\n\
        1 - For å sjekke saldo,\n\
        2 - For uttak,\n\
        3 - For innskudd, \n\
        x - For å avslutte.")

def meny():
    inp = input(">")
    if inp == "1":
        sjekk_saldo()
        meny()

    elif inp == "2":
        ta_ut()
        meny()
    elif inp == "3":
        sett_inn()
        meny()
    elif inp != "x":
        print("Ukjent kommando, prøver igjen\n")
        kommandoer()
        meny()
    else:
        print("Ha en fin dag videre!")

kommandoer()
meny()
