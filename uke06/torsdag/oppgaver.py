# Oppgave 1
def minus():
    a = 3
    b = 2


def summer():
    print("sum: ", a + b)

def oppgave1():
    summer()


# A) Fungerer programmet ovenfor?
# B) Endre programmet slik at det fungerer. Dere skal ikke bruke globale variabler. 


# Oppgave 2
def legg_til_bokstav(ordliste, bokstav):
    for ord in ordliste:
        ord += bokstav
    return ordliste


def oppgave2():
    ordliste = ["Je", "de", "se"]
    ordliste = legg_til_bokstav(ordliste, "g")
    print(ordliste)

# A) Hvorfor endres ikke ordene i programmet ovenfor? 
# B) Endre programmet slik at ordene endres. Dere skal ikke bruke globale variabler. 



# Oppgave 3
def oppgave3():
    grense = -5
    grenseteller = 0


    while grenseteller <= 0:
        print("Har vi nådd grensen?", grenseteller == grense)
        grenseteller -= 1

# A) Hvorfor slutter programmet ovenfor aldri å kjøre? Diskuter.
# B) Endre programmet slik at det stopper (terminerer) når grensa (grense) er nådd. Dere skal ikke bruke globale variabler. 


# Oppgave 4
def bygg_samling(antall_rader, antall_kolonner):
    samling = []

    while antall_rader > 0:
        rad = []
        for kolonnenr in range(antall_kolonner):
            rad.append(kolonnenr)
       
        samling.append(rad)
        antall_rader -= 1

    return samling


def oppgave4():
    samling = bygg_samling(7, 5)

# A) Hva slags samling er det programmet ovenfor bygger, og hvordan ser samlingen ut? Diskuter uten å kjøre programmet.
# B) Hva er oppgaven til while-løkka og hva er oppgaven til for-løkka? Diskuter.
# C) Utvid programmet med en funksjon, finn_antall, som tar inn den bygde samlingen og et tall.
# Funksjonen skal returnere antall ganger det oppgitte tallet finnes i samlingen. Hovedprogrammet skal skrive ut dette antallet.


# Oppgave 5
def hent_navn(personbok, personid):
    if personid in personbok:
        return personbok[personid]
    return None


def oppgave5():
    personbok = {
        "01020300000": "Hjørdis Olsen",
        "02030400000": "Martin Halvorsen",
        "03040500000": "Kristin Andersen"
    }


    personid = "02030400000"
    navn = hent_navn(personbok, personid)
    startbokstav = "M"


    if navn:
        print("Fant person ved navn", navn + ".")
        if navn[0] == startbokstav:
            print("Navnet starter på", startbokstav + ".")
    else:
        print("Fant ingen person med id", personid + ".")


# Hva skrives ut i programmet ovenfor? Diskuter først uten å kjøre koden.
# Hva skrives ut hvis personid ikke finnes i personbok?
# Endre programmet, slik at det ikke lenger inkluderer nøstede beslutninger. Programmet skal likevel gjøre det samme etter endringen som før endringen.

