# Oppgave 1

Per, Palle og Espen lurer på om de skal finne på noe til kvelden. Dersom nøyaktig to av dem ønsker å spille badminton går de for det, men ellers (om færre enn to eller flere enn to vil dette) gjør de heller noe annet.

Skriv en funksjon, badminton(per_vil, palle_vil, espen_vil), som tar inn tre boolske argumenter, og returnerer True dersom to (og kun to) av de tre argumentene er True.

Altså skal for eksempel kallet badmington(True, True, False) returnere True, mens kallet badmington(True, True, True) skal returnere False.

---

# Oppgave 2

Skriv en funksjon, summer_rabatt(vareliste, førpris, nypris). Den tar som argument en liste med varenavn (vareliste), en ordbok med varenavn som nøkler og førprisen som verdier (førpris), samt en ordbok med varenavn som nøkler og nyprisen som verdier (nypris).

Funksjonen skal regne ut hvor mye rabatt en kunde har fått i sum dersom kunden har kjøpt varene i vareliste (én av hvert element i lista). Rabatten for en gitt vare er forskjellen mellom førpris og nypris for det gitte varenavnet, hvor disse prisene ligger i hver sin ordbok førpris og nypris. Du kan anta at alle varenavn i vareliste finnes som nøkler i både ordboken førpris og nypris, og du kan anta at nypris alltid er lavere eller lik førpris.

For eksempel skal kallet summer_rabatt(["laptop", "ryggsekk"], {"laptop":5000, "ryggsekk":900}, {"laptop":4000, "ryggsekk":600}) returnere 1300.

---

# Oppgave 3

Du er medgangssupporter for fotballaget Brann. Det betyr at så lenge Brann gjør det ganske bra heier du på dem. Om de gjør det veldig dårlig, er du kynisk og velger heller å heie på laget som leder på tabellen.

Skriv en funksjon, heie(tabellplass_ordbok), som tar som argument en ordbok hvor nøklene er navn på fotballag og verdiene er plassering på tabellen. Dersom verdien i ordboka for nøkkelen "Brann" er 3 eller mindre, skal funksjonen returnere strengen "Brann". Ellers skal funksjonen returnere nøkkelen som i ordboka er koblet til verdien 1. Du kan anta at nøkkelen "Brann" finnes i tabellplass_ordbok, og du kan anta at tabellplass_ordbok har et lag med verdi 1.

Altså skal kallet heie({"Rosenborg":4, "Odd":1, "Molde":3, "Brann":2}) returnere "Brann", mens kallet heie({"Rosenborg":2, "Odd":1, "Molde":3, "Brann":4}) skal returnere "Odd".

---

# Oppgave 4

Tenk at dere har fått utdelt en fil med gruppeoppmøte i IN1000. Filnavn: oppmøte\_in1000.txt. Skriv et program som ved hjelp av en funksjon leser inn filen og skriver ut gruppene som har hatt 20 eller flere oppmøtte studenter i uke 11. Funksjonen har filnavn som parameter.
Første linje i filen består av gruppenummer: gruppe\_1, gruppe\_2, gruppe\_3, o.s.v., til og med gruppe\_8. Gruppene er atskilte med ; (semikolon). På linjene nedenfor står antall oppmøtte i hver gruppe per uke. Antallene er atskilte med ; (semikolon). Andre linje i fila har oppmøteantall for uke 1, tredje linje i fila har oppmøte for uke 2, o.s.v., til og med uke 12.
Her er et eksempel på hvordan de to første linjene i oppmøte\_in1000.txt kan se ut:

gruppe\_1; gruppe\_2; gruppe\_3; gruppe\_4; gruppe\_5; gruppe\_6; gruppe\_7; gruppe\_8

10; 19; 25; 18; 23; 11; 13; 17

Forsøk først å lage et python-program som generer denne listen for deg (slik at du ikke manuelt må skrive inn hver linje). Det ligger et ferdig program [her](./generer_oppmotefil.py) som gjør dette for deg.

---

# Oppgave 5

Et land har følgende regler for reisekarantene:
Dersom en person er vaksinert, trenger personen ikke å gå i karantene (0 dager i karantene)
Dersom en uvaksinert person har vært i et land som har fargekode rød eller oransje, skal personen 10 dager i karantene.
Dersom en uvaksinert person har vært i et land som har fargekode grønn, skal personen 3 dager i karantene.

Skriv en funksjon, karantene(vaksinert, farge), som returner antall dager (heltall) en person må i karantene i henhold til reglene ovenfor. Parameteren vaksinert er enten True eller False (boolsk verdi) og parameteren farge er enten "rød", "oransje" eller "grønn" (streng).

Altså skal for eksempel kallet karantene(True, "roed") returnere 0, mens kallet karantene(False, "oransje") skal returnere 10.

Utvid programmet i a), slik at det leser inn en fil ved navn karantene.txt. Hver linje i filen består av vaksinasjonsstatusen til en person (True eller False) og fargen på landet de har vært i (rød, oransje eller grønn). Vaksinasjonsstatus og farge er atskilt med komma. Videre skal programmet summere og skrive ut antall karantenedager fra henholdsvis røde, oransje og grønne land (antall for hver farge separat samt antall karantenedager totalt).

---

# Oppgave 6

Du ønsker hjelp til å gruppere sammen personer som har felles interesse.

Skriv en funksjon, lag_interessegrupper(personers_interesse), som tar som argument en ordbok hvor nøklene er strenger som er navn på personer, mens hver verdi er en streng som sier hvilken interesse personen har.

Funksjonen skal returnere en ordbok, hvor hver nøkkel er en interesse (streng) og hver verdi er en liste av personer som var oppført med denne interessen i ordboken personers_interesse. Alle interessene som finnes i ordboken personers_interesse skal være med i den returnerte ordboken.

Altså skal for eksempel kallet lag_interessegrupper({"Per":"Mat", "Palle":"Film", "Espen":"Mat"}) evaluere til ordboken {"Mat":["Per","Espen"], "Film":["Palle"]}

Utvid programmet i a), slik at det lager en fil med interesser og antall personer som har hver interesse. Hver linje skal bestå av interesse og antall, atskilt med komma. Filen skal hete interesseantall.txt.

---

# Oppgave 7 Ekstra utfordring

Definer en funksjon, sjekk_reise(reise), som tar inn en nøstet liste reise. Hvert element i den nøstede lista er igjen en liste med to strenger (et par av reiseopprinnelse og reisemål). Funksjonen skal returnere True dersom reise er en gyldig reiserute, og False ellers. Reiseruten er gyldig når hvert reisemål (andre element i en indre liste) er likt reiseopprinnelsen (første element) i den etterfølgende indre listen. Du kan anta at alle elementene i den ytre listen er en indre liste av lengde 2.

For eksempel skal kallet sjekk_reise([["Spania", "Frankrike"], ["Frankrike", "Norge"]]) returnere True da den beskriver reisen Spania -> Frankrike -> Norge. Kallet sjekk_reise([["Russland", "Tyskland"], ["Tyskland","Sverige"], ["Norge", "Belgia"]]) skal derimot returnere False, fordi andre etappe ender i Sverige mens neste etappe starter i Norge. Merk at også listen [["Russland", "Tyskland"], ["Norge", "Tyskland"]] skal returnere False, fordi den andre etappen skulle ha startet i Tyskland (i stedet slutter den der, og er dermed ikke gyldig).
