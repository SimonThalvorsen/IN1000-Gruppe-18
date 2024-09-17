intro = ["Per", "Pål", "Espen", "Kari", "Trude"]
ekstro = ["Andrea", "Karl", "Amalie", "Guro", "Johann"]


bord = []
# Så lenge listen ikke er tom
while intro:
    # antar at begge listen er like lange
    bord.append(intro.pop(0))
    bord.append(ekstro.pop(0))

print(bord)

# Range(len - 1) fordi vi øker med 1 for å finne neste, dette gjør at vi ikke går over lengden til listen
for i in range(len(bord)-1):
    print(bord[i], bord[i+1])
