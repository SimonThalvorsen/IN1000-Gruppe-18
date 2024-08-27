streng_en = "eple"
streng_to = "pære"
streng_tre = "banan"

inp = input("Skriv inn en frukt\n>")
inp2 = input("Skriv inn enda en frukt\n>")


if (inp == streng_en and inp2 == streng_to) or (inp == streng_to and inp2 == streng_en):
    print(f"Du skrev inn {streng_en} og {streng_to}")
elif (inp == streng_to and inp2 == streng_tre) or (inp == streng_tre and inp2 == streng_to):
    print(f"Du skrev inn {streng_tre} og {streng_to}")
elif (inp == streng_en and inp2 == streng_tre) or (inp == streng_tre and inp2 == streng_en):
    print(f"Du skrev inn {streng_en} og {streng_tre}")
else:
    print("Du skrev ikke inn noen av fruktene.")
