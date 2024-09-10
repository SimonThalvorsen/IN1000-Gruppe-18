p1 = ["Simon", "Vestgrensa", "473 37 723","Italia"]
p2 = ["Iselin","Pilestredet", "123 12 123", "Lofoten"]
p3 = ["Thomas", "Bjølsen", "123 12 123","Lofoten"]
p4 = ["Nora", "Bislett", "456 67 456", "Spania"]
p5 = ["Embrik","Bjølsen", "612 44 17", "England"]

reisende = {12345678900: p1, 343247893266: p2, 63927162961: p3, 35326782347: p4, 79318272361: p5}

inp = input("Passsjekk, tast inn personnr.\n>")
inp = int(inp)
if inp in reisende:
    print(f"Informasjon om {inp}:\n")
    # print(reisende[inp])

    print(f"Navn: {reisende[inp][0]},")
    print(f"Adresse: {reisende[inp][1]},")
    print(f"Tlf.nr.: {reisende[inp][2]},")
    print(f"Destinasjon: {reisende[inp][3]}")
else:
    print("Denne personen reiser ikke med oss.")
