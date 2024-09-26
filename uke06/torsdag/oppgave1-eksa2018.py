# A
"""
Hva er verdien til tall etter at følgende kode er utført?
tall = (3+1) * 2
tall = tall - 5
"""
def opg1a():
    print("Hva er verdien til tall etter at følgende kode er utført?\ntall = (3+1) * 2\ntall = tall - 5")
    svar = input()
    tall = (3+1) * 2
    tall = tall - 5
    if int(svar) == tall:
        print("Korrekt!")
    else:
        print("feil svar")

opg1a()

print()

def opg1b():
    print("""Hva er verdien til variabelen tekst etter at følgende kode erutført?
tall = 7
tekst = "a"
if tall>10:
    tekst = tekst + "b"
elif tall<5:
    tekst = tekst + "c"
else:
    tekst = tekst + "d""") 
    tall = 7
    tekst = "a"
    if tall>10:
        tekst = tekst + "b"
    elif tall<5:
        tekst = tekst + "c"
    else:
        tekst = tekst + "d"
    svar = input()
    if svar == tekst:
        print("Korrekt")
    else:
        print("Feil svar :(")

opg1b()

print()

def opg1c():
    print("""
Hva er verdien til variabelen a etter at følgende kode er utført?
a = 0
for b in [2,4,1]:
    a = 2*a + b
""")

    a = 0
    for b in [2,4,1]:
        a = 2*a + b
    svar = int(input())
    if svar == a:
        print("Korrekt")
    else:
        print("Feil svar :(")

opg1c()

print()

def opg1d():
    print("""Hva skrives ut på skjermen når følgende kode utføres?
tallene = [ ]
a = 0
b = 1
while a<4:
    tallene.append(b)
    b = b*2
    a = a+1
print(tallene[0] + tallene[3])""")
    tallene = [ ]
    a = 0
    b = 1
    while a<4:
        tallene.append(b)
        b = b*2
        a = a+1
    # print(tallene[0] + tallene[3])
    fasit = tallene[0] + tallene[3]
    svar = int(input())
    if svar == fasit:
        print("Korrekt")
    else:
        print("Feil svar")

opg1d()
print()

def opg1e():
    print("""Vi har en funksjon kalkuler som vist nedenfor:
def kalkuler(tall):
    tall = tall + 1
    return tall*2

Hva skrives ut på skjermen når følgende kode utføres?
print( kalkuler(2) + kalkuler(4) )""")

    def kalkuler(tall):
        tall = tall + 1
        return tall*2
    # print( kalkuler(2) + kalkuler(4) )
    fasit = kalkuler(2) + kalkuler(4)
    svar = int(input())
    if svar == fasit:
        print("Korrekt")
    else:
        print("feil")

opg1e()
print()

## NOTE: Dere har ikke lært dette enda, men tar den med bare for å vise veldig kjapt hva dere skal lære neste uke
def opg1f():
    print("""
class Tall:
    def __init__(self, a):
        self._a = a
    def m1(self, c):
        self._a = self._a + c
    def m2(self):
        self._a = self._a * 2
    def m3(self):
        return self._a + 10
t1 = Tall(5)
t2 = Tall(2)
t1. m2()
t2.m1( t1.m3() )
print( t2.m3() )""")

    class Tall:
        def __init__(self, a):
            self._a = a
        def m1(self, c):
            self._a = self._a + c
        def m2(self):
            self._a = self._a * 2
        def m3(self):
            return self._a + 10
    t1 = Tall(5)
    t2 = Tall(2)
    t1. m2()
    t2.m1( t1.m3() )
    # print( t2.m3() )
    fasit = t2.m3()
    svar = int(input())
    if svar == fasit:
        print("RIKTIG")
    else:
        print("Feil :(")

opg1f()

