streng_en = "eple"
streng_to = "pære"
streng_tre = "banan"

inp = input("Skriv inn en frukt\n>")
inp2 = input("Skriv inn enda en frukt\n>")

if inp2 == streng_en:
    print(f"Du skrev inn {streng_en} Du kan skrive")
elif inp2 == streng_to:
    print("Du skrev inn " + streng_to)
elif inp2 == streng_tre:
    print("Du skrev inn " + streng_tre)
else:
    print("Du skrev ikke inn en frukt")

if inp == streng_en:
    print(f"Du skrev inn {streng_en} Du kan skrive")
elif inp == streng_to:
    print("Du skrev inn " + streng_to)
elif inp == streng_tre:
    print("Du skrev inn " + streng_tre)
else:
    print("Du skrev ikke inn en frukt")

