potetgull = ["Kims", "Superchips", "Sørlandschips", "Maarud", "Lay's", "Pringles", "Gårdschips", "Totenflak"]

inp = input("Skriv inn et potetgull-merke\n>")

if inp.lower().capitalize() in potetgull:
    print("Gjenkjent!")
else:
    print("Det forstor jeg ikke.")
