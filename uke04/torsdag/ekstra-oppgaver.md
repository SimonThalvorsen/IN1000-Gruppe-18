# Oppgave 1

A) Forklar hva som skjer i programmet under.

```python3
x = 3
while x < 10:
   x += 1
   print(x)
```

B) Når slutter while-løkka å kjøre og hvorfor?

# Oppgave 2

Hva skrives ut på skjermen i programmet under? Kom frem til et svar før dere kjører programmet. Kjør også programmet i Python Tutor. Her kan det være nyttig å skrive ned verdiene av a og b for hver runde løkka kjører (det vil si for hver iterasjon).

```python3
a = 10
b = 1

while a > 0:
  b = b * 2
  a = a - b

print("a =", a)
print("b =", b)
```

# Oppgave 3

Skriv et program som har en variabel a med verdien 1 og en while-løkke. For hver runde (hver iterasjon) i while-løkka skal variabelen a adderes med 2. Løkka skal være ferdig når verdien av a er større enn 100. Skriv så ut verdien av a. Når sjekkes betingelsen i while-løkka for siste gang, og hvorfor slutter while-løkka da å kjøre?

# Oppgave 4

Skriv et program som inneholder en while-løkke. Inne i løkka skal bruker bes om å taste et tall. Dersom tallet ikke er 10, skal løkka fortsette å be om tall. Når bruker taster inn tallet 10, skal vedkommende få beskjeden “Du har tastet inn tallet 10. Programmet avsluttes …”, før programmet så avslutter.

Utfordring: summer alle tallene brukeren skriver inn frem til 10 blir tastet. Når 10 tastes inn, skrives summen av tallene (ikke inkludert 10) ut. Med andre ord; hvis bruker taster sekvensen 1, 3, 4 og 10, skrives “Sum er: 8” før programmet avslutter.

# Oppgave 5

A) Hva skrives ut i terminalen ved kjøring av programmet under? Kom frem til et svar før dere kjører programmet. Kjør programmet også i Python Tutor.

```python3
tekst = ["hadet", "på", "badet", "din", "gamle", "sjokolade"]
indeks = 0

while indeks < len(tekst):
print(tekst[indeks])
indeks += 2
```

B) Hvorfor oppstår det feil hvis dere bytter ut < med <= i løkkebtingelsen over?
C) Hva slags løkke ville dere valgt hvis dere skulle skrevet ut alle ordene i lista? Diskutér, og lag deretter et program som skriver ut alle ordene.

# Oppgave 6

Dere har listen:

```python3
artister = ["Taylor Swift", "Knocked Loose", "Bruno Mars"].
```

Print ut alle elementene i lista med en for-løkke ved:

A) Å løpe (iterere) gjennom lista uten å bruke listeeindekser. Beskriv all koden og hva som endrer seg underveis i kjøringen.

B) Å løpe (iterere) gjennom lista ved å bruke listeeindekser. Beskriv all koden og hva som endrer seg underveis i kjøringen.

C) Sammenlign de to variantene av for-løkke i a og b. Hva oppdager dere?

# Oppgave 7

Gitt følgende liste:

```python3
tegnliste = ["h", "e", "i", ",", " ", "d", "u", "!"]
```

A) Bruk en for-løkke og lag en setning med tegnene. Dere kan anta at tegnene står i riktig rekkefølge i tegnliste. Skriv ut setningen i terminalen til slutt.

B) Lag en mengde av tegnliste. Gjør så det samme som dere gjorde i a), men ved å bruke mengden i stedet for. Hva oppdager dere, og hvorfor er det slik?

# Oppgave 8

Skriv et program med en prosedyre, print_hei. Prosedyren skal skrive ut teksten “Hei” til terminalen. Bruk så en løkke, som kaller prosedyren print_hei. Når løkken er ferdig, skal “Hei” ha blitt skrevet ut fem ganger.

A) Skriv prosedyren print_hei. Løs så oppgaven ved hjelp av en while-løkke, deretter en for-løkke.

B) Hvilken av de to løkkene anser dere som best egnet til å løse oppgaven? Diskutér fordeler og ulemper.
