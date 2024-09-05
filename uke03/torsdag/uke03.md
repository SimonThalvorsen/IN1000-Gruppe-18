# Tjenester (metoder) til objekter

- Noe som kan utføres PÅ et objekt.
- Variable holder på referanse/peker/verdi til et objekt.
- Objekt.metode() - metoden kalles PÅ objektet, gjøres med en . mellom det spesifiserte objektet og metoden.

# Lister []

- Kan holde på flere verdier, eks. liste = [1, 2, 3, 4, 5, 6, 7]
- Indeksert, begynner telling på 0, dvs. liste[0] -> 1, liste[1] -> 2 ... osv
- Indeksen "-1" er alltid det siste elementet i listen. liste[-1] -> 7
- Lister har mange metoder, se: [w3schools.com/python/list_methods](https://www.w3schools.com/python/python_lists_methods.asp)
- Lister kan holde elementer/objekter (integers, floats, strings, lister, ordbøker, sett osv.)

# Mengder

- Samling av unike elementer.
- I motsetning til lister kan mengder kun inneholde verdier som kan gjøres om til en unik identifikator.

  - Dvs. mengder kan ikke inneholde muterbare (elementer som kan endre seg, typ lister og ordbøker) objekter.

- a = set() # Lager en tom mengde
- a = {1, 2, 3} # Lager en mengde med elementene 1, 2, 3
- a = list(set(a)) # Fjerner duplikater

# Ordbøker

- Mapping av nøkler til verdi (key/value-pairs). Se for deg en faktisk ordbok eller en telefonkatalog.
- Ordbøker, i likhet med mengder må ha en unik identifikator på nøkkelen.
- Nøkkel må være unik, verdi kan være hva som helst.

- ordbok = {} # Lager en tom ordbok
- ordbok = {"Keyboard": "Tastatur"} # Lager en ordbok med nøkkelen "Keyboard" som refererer til verdien "Tastatur"
- Har også en god del metoder, se: [w3schools.com/python/list_methods](https://www.w3schools.com/python/python_dictionaries_methods.asp)

## Generelt

- Samlinger og metoder kan være vanskelig i begynnelsen, min anbefaling er å teste MYE, for å lage seg en god forståelse for hva som foregår.
- Hvilke type samling og hvilke metoder som er nyttige kommer med erfaring. Derfor det bare er å komme i gang!
- Mye info på [w3schools.com/python](https://www.w3schools.com/python/), se høyre side for temaer.
