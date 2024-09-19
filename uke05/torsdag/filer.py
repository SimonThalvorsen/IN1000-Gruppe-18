# Oppgave 5
# Anta at du har filen “historiske_personer.txt”.
#
# A) Les inn alle linjene og lagre dem i en liste. Første historiske person (linje) i filen skal ligge først i lista, o.s.v. 
# Tips: husk å åpne og lukke filen.
#
# B) Opprett filen “historiske_personer.txt”. Fyll den med noen historiske personer ved å skrive direkte i fila. Legg fila i samme mappe som .py-filen din.
#
# C) Test at programmet fra a) fungerer ved å bruke filen du opprettet i b).

# fil = open("historiske_personer.txt", "r")
# liste = []
# for linje in fil:
#     liste.append(linje)
# fil.close()


#
# Oppgave 6
# Lag et program som skriver historiske personers navn og fødselsår til fil. Navnene og fødselsårene skal være lagret i en ordbok,
# med navn som nøkler og fødselsår som verdier.
# Tips: husk å åpne og lukke filen ved behov.
#
# Opprett en ordbok med fem historiske personer og deres fødselsår.
#
# Skriv navn og fødselsår til fil. Hver linje skal ha en historisk persons navn og fødselsår, atskilt med ; (semikolon). 
# Filen skal hete “historiske_personer_fodt.txt”. 
#
# Lag et nytt program, som bruker en funksjon til å lese inn filen du laget i b) og som returnerer en ordbok tilsvarende den i a). 
# Funksjonen skal ha parameter filnavn. 

ordbok = {"Simon blir født":2002, "Norge får grunnlov":1814, "Krigen er over":1918, "Krigen er over (2)": 1945}

filnavn = "historiske_hendelser"

def lag_tekst_fil(filnavn, ordbok):
    fil = open(filnavn, "w")
    for key in ordbok:
        fil.write(key)
        fil.write(";")
        fil.write(str(ordbok.get(key)))
        fil.write("\n")

        # print(key)
        # print(ordbok.get(key))
    fil.close()

lag_tekst_fil(filnavn, ordbok)



