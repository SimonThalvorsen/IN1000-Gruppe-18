streng_en = "eple"
streng_to = "pære"
streng_tre = "banan"

inp = input("Skriv inn en frukt\n>")
inp2 = input("Skriv inn enda en frukt\n>")

if inp == streng_en or inp == streng_to or inp == streng_tre:
    print(f"Du skrev inn {inp}")
if inp2 == streng_en or inp2 == streng_to or inp2 == streng_tre:
    print(f"Du skrev inn {inp2}")
else:
    print("Du skrev ikke inn noen av fruktene")