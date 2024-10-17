from bibliotek import Bibliotek
from bok import Bok


def main():
    bibliotek = Bibliotek()
    bibliotek.les_fra_fil("books.txt")

    hobbit = bibliotek.finn_bok("The Hobbit")
    hobbit.laan_ut()

    boker = bibliotek.finn_boker("the")
    print(boker)
    print(sorted(boker))

    bok1 = Bok("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 123456789)
    bok2 = Bok("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 112233445)
    print(bok1 == bok2)

    for bok in boker:
        print(bok)
        if bok.er_tilgjengelig():
            print(bok.hent_tittel(), "er tilgjengelig for utlån.")
        else:
            print(bok.hent_tittel(), "er utlånt.")


main()
