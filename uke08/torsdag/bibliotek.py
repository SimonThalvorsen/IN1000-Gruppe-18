from bok import Bok
    # Søke etter bøker ✔
    # Søke etter forfatter ✔
    # Sjekke status bok ✔
    # Legge til bøker ✔
    # Låne ut bøker ✔
class Bibliotek:
    def __init__(self):
        self._boker = []

    def legg_til_bok(self, bok: Bok):
        self._boker.append(bok)

    def les_fra_fil(self, filnavn: str):
        # Format = navn;tittel;isbn
        fil = open(filnavn, "r")
        for line in fil:
            tekst = line.strip().split(";")
            bok = Bok(tekst[1], tekst[0], tekst[2])
            self.legg_til_bok(bok)
        fil.close()

    def finn_bok(self, tittel: str):
        bok = None
        for e in self._boker:
            if e.hent_tittel() == tittel:
                bok = e

        if bok is None:
            print("Fant ikke boken")
            return None
        else:
            return bok
        

    def finn_boker(self, tittel: str):
        boker = []
        for bok in self._boker:
            if bok.tittel_inneholder(tittel):
                boker.append(bok)
        return boker

    def finn_boker_fra_forfatter(self, forfatter: str):
        boker = []
        for bok in self._boker:
            if bok.hent_forfatter() == forfatter:
                boker.append(bok)
        return boker

