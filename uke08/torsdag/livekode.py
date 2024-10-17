from bibliotek import Bibliotek

def main():
    bibliotek = Bibliotek()
    bibliotek.les_fra_fil("books.txt")
    
    hobbit = bibliotek.finn_bok("The Hobbit")
    hobbit.laan_ut()

    boker = bibliotek.finn_boker("the")
    for bok in boker:
        if bok.er_tilgjengelig():
            print(bok.hent_tittel(), "er tilgjengelig for utlån.")
        else:
            print(bok.hent_tittel(), "er utlånt.")
    
    

main()
