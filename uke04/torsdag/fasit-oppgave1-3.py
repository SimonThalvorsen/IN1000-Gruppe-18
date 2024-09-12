# Under finner du en vanlig handleliste og en ordbok som peker til pris per vare. 

# Det er totalt 3 oppgaver, for hver av oppgave skal du bruke den løkken som best egner
# seg til å løse oppgaven basert på det vi nå har gjennomgått i gruppetimen.


handleliste = [
    "Epler",
    "Bananer",
    "Appelsiner",
    "Brokkoli",
    "Gulrøtter",
    "Brød",
    "Melk",
    "Egg",
    "Ost",
    "Kyllingfilet",
    "Pasta",
    "Tomatsaus",
    "Olivenolje",
    "Ris",
    "Hermetiske bønner"
]


priser_per_vare = {
    "Epler": 20.0,
    "Bananer": 15.0,
    "Appelsiner": 25.0,
    "Brokkoli": 18.0,
    "Gulrøtter": 12.0,
    "Brød": 25.0,
    "Melk": 20.0,
    "Egg": 30.0,
    "Ost": 50.0,
    "Kyllingfilet": 90.0,
    "Pasta": 15.0,
    "Tomatsaus": 10.0,
    "Olivenolje": 70.0,
    "Ris": 20.0,
    "Hermetiske bønner": 12.0
}

# Oppgave 1:
# Skriv ut hver vare i handlelisten i riktig rekkefølge og skriv samtidig ut hvilken
# posisjon i handlelisten du finner den i.
def oppgave1():
    for vare in handleliste:
        print(f"{vare} ligger på posisjon {handleliste.index(vare)} i handlelisten.")


def oppgave1_2():
    pos = 0
    for vare in handleliste:
        print(f"{vare} ligger på posisjon {pos} i handlelisten.")
        pos += 1

# Oppgave 2:
# Du skal nå gå gjennom hele listen fra start helt til du finner elementet 'Ost'. 
# Når du finner Ost skal du skrive "Ost ligger i listen" og avslutte programmet.
def oppgave2():
    idx = 0
    vare = handleliste[idx]

    while vare != "Ost":
        idx += 1
        vare = handleliste[idx]

    print("Ost ligger i listen")

def oppgave2_2():
    for vare in handleliste:
        print(vare)
        if vare == "Ost":
            print("Ost ligger i listen")
            break





# Oppgave 3:
# Du skal nå gå gjennom alle prisene per vare og skrive ut oversiktlig hva hver vare koster.
# Du skal ikke bruke listen med matvarer som hjelp, kun jobbe på ordboken.
def oppgave3():
    for vare in priser_per_vare:
        print(f"{vare} koster {priser_per_vare[vare]} kroner.")
