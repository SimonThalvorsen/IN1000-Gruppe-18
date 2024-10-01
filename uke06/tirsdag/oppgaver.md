# Oppgave 1

Skriv en funksjon, tell_grader(fag, bsc, msc), som tar inn tre argumenter av datatypen string og sjekker om en bachelorgrad (bsc) og/eller en mastergrad (msc) er innen et bestemt fag.

Dersom fag har samme verdi som bsc og msc, skal funksjonen returnere 2. Dersom fag har samme verdi som enten bsc eller msc, skal funksjonen returnere 1. Dersom fag hverken er lik bsc eller msc, skal funksjonen returnere 0.

For eksempel skal kallet tell_grader("informatikk", "informatikk", "informatikk") returnere 2, mens kallet tell_grader("historie", "informatikk", "informatikk") skal returnere 0. Test funksjonen med flere eksempler på fag, bsc og msc i et hovedprogram som er definert som hovedprogram().

---

# Oppgave 2

Skriv en funksjon, forkort_lagliste(lagliste), som tar som argument en liste av strenger som er lagnavn og returnerer en ny liste hvor ingen lagnavn finnes flere ganger i lista.

Med andre ord, dersom samme streng opptrer flere ganger i lista som funksjonen mottar som argument, skal denne bare opptre én gang i lista som blir returnert.

For eksempel skal kallet forkort_lagliste(["Brann", "Molde", "Brann"]) returnere en liste ["Brann", "Molde"]. Test funksjonen med flere eksempler på lagliste i et hovedprogram som er definert som hovedprogram().

# Oppgave 3

Programmet nedenfor leser inn fra tekstfil hvor mye henholdsvis Peter og Pål har hatt i ferieutgifter. Koden kjører og gir riktig svar, men det er en del unødvendige gjentakelser.

Du skal skrive en modifisert versjon av programmet, slik at det skriver ut det samme som det opprinnelige, men med færre gjentakelser i koden.

```python
def hovedprogram():
    fn_peter = "Peter.txt"
    tot_peter = 0

    for line in open(fn_peter):
        utgift_peter = int(line)
        tot_peter += utgift_peter
        print("Peter har brukt: ", tot_peter)


    fn_paul = "Paul.txt"
    tot_paul = 0
    for line in open(fn_paul):
        utgift_paul = int(line)
        tot_paul += utgift_paul
        print("Paul har brukt: ", tot_paul)

hovedprogram()
```

---

# Oppgave 4

Skriv en funksjon, fjern_vokaler(setning, vokalliste), som tar inn en setning (datatype string) og en liste med vokaler (hvor hvert element i lista er en string av lengde 1).

Funksjonen skal returnere en kopi av setning, hvor alle vokaler fra vokalliste er fjernet. Du kan anta at både setning og vokalliste kun inneholder små bokstaver.

For eksempel skal kallet fjern_vokaler("ha det fint", ["a", "e", "i", "o", "u"]) returnere teksten "h dt fnt". Test funksjonen med flere eksempler på setning og vokalliste i et hovedprogram som er definert som hovedprogram().

---

# Oppgave 5

Skriv en funksjon, er_sortert(talliste), som tar en liste med tall som argument og som returnerer en boolsk verdi.

Funksjonen skal sjekke om alle tallene i lista er i stigende rekkefølge (sorterte). Dersom alle verdiene er i stigende rekkefølge, skal funksjonen returnere True, ellers skal funksjonen returnere False. Anta at alle tallene i lista er ulike. Funksjonen trenger altså ikke ta hensyn til eventuelle like verdier.

For eksempel skal er_sortert([2, 4, 6, 8, 10]) returnere True og er_sortert([7, 3, 1, 9]) returnere False. Test funksjonen med flere tallister i et hovedprogram som er definert som hovedprogram().

---

# Oppgave 6

Denne oppgaven bygger videre på oppgave 5 ovenfor. Lag et hovedprogram som legger inn alle sorterte lister i én ordbok og alle usorterte lister i en annen ordbok. Nøklene i ordboka for de sorterte listene er på formen 1s, 2s, 3s, o.s.v. I ordboka for de usorterte listene er nøklene på formen 1u, 2u, 3u, o.s.v.

Når de to ordbøkene er laget, skal dere bruke ordbøkene til å lage en liste med lengde lik 2. Det første elementet i lista er en liste med sorterte lister, og det andre elementet i lista er en liste med usorterte lister.

Til slutt skal programmet skrive ut en oversikt over de sorterte listene og en oversikt over de usorterte listene. Husk passende overskrifter i utskriften, og sørg for at hver av listene skrives ut på nye linjer. Dere skal ikke skrive ut elementene i de sorterte og usorterte listene - bare de sorterte og usorterte listene i seg selv.
