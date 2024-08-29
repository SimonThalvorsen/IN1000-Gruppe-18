def prosedyre1():
    print("Hei fra prosedyre 1!")
    prosedyre2()

def prosedyre2():
    tall = int(input("Skriv inn et tall\n>"))
    if tall % 2 == 0:
        prosedyre1()
    else:
        prosedyre3()
    

def prosedyre3():
    tall = int(input("Skriv inn et tall\n>"))
    if tall > 10:
        prosedyre1()

prosedyre1()
