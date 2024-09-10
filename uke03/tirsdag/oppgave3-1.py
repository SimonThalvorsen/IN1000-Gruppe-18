p1 = {"navn": "Simon", "adresse":"Vestgrensa", "tlf": "473 37 723", "dest":"Italia"}
p2 = {"navn": "Iselin", "adresse":"Pilestredet", "tlf": "123 12 123", "dest":"Lofoten"}
p3 = {"navn": "Thomas", "adresse":"Bjølsen", "tlf": "987 12 987", "dest":"Bergen"}
p4 = {"navn": "Nora", "adresse":"Bislett", "tlf": "456 67 456", "dest":"Spania"}
p5 = {"navn": "Embrik", "adresse":"Bjølsen", "tlf": "612 44 17", "dest":"England"}

reisende = {12345678900: p1, 343247893266: p2, 63927162961: p3, 35326782347: p4, 79318272361: p5}

inp = input("Passsjekk, tast inn personnr.\n>")
inp = int(inp)
if inp in reisende:
    print(f"Informasjon om {inp}:\n")
    # print(reisende[inp])

    print(f"Navn: {reisende[inp]["navn"]},")
    print(f"Adresse: {reisende[inp]["adresse"]},")
    print(f"Tlf.nr.: {reisende[inp]["tlf"]},")
    print(f"Destinasjon: {reisende[inp]["dest"]}")
else:
    print("Denne personen reiser ikke med oss.")


