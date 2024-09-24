def opprett_filen():
    fil = open("test.in", "w")
    for i in range(10):
        #fil.write("Test " + str(i) + "\n")
        fil.write(f"Test {i}\n")
    fil.close()

def skriv_ut_foerste_linjer(filnavn, ant_linjer):
    fil = open(filnavn, "r")
    for _ in range(ant_linjer):
        linje = fil.readline().strip("\n")
        print(linje)
    fil.close()

def skriv_ut_siste_linjer(filnavn, ant_linjer):
    fil = open(filnavn, "r")
    alle_linjer = fil.readlines()
    for _ in range(ant_linjer):
        linje = alle_linjer.pop()
        print(linje.strip("\n"))
    fil.close()

opprett_filen()

skriv_ut_foerste_linjer(filnavn="test.in", ant_linjer=3)
print()
skriv_ut_siste_linjer(filnavn="test.in", ant_linjer=3)




