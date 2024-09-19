# Funksjoner (Prosedyrer med en returverdi og/eller argumenter)
def carbonara():
    return "Carbonara"

def brus(glass):
    glass.append("Brus")
    return glass


"""tallerken = carbonara()
glass = []

brus(glass)

print(tallerken, glass)"""

# string = "Heisann"
# print(string.count("n"))


def count(samling, ting):
    teller = 0
    for e in samling:
        if ting in e:
            teller += 1
    return teller







# Filer (Lese fra fil, skrive til fil, lage fil)
fil = open("filer.txt", "r")
for linje in fil:
    print(linje)

fil.close()

with open("filer.txt", "r") as fil:
    for linje in fil:
        print(linje)




