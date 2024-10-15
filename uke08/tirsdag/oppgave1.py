class Rektangel:
    def __init__(self, bredde, lengde):
        self._bredde = bredde
        self._lengde = lengde

    def areal(self):
        return self._lengde * self._bredde

class Leilighet:
    def __init__(self, rom):
        self._rom = rom

    def skriv_areal_leilighet(self):
        areal = 0
        for rom in self._rom:
            areal += rom.areal()

        print(areal)

def main():
    alle_rom = [Rektangel(5, 4), Rektangel(3, 3), Rektangel(4, 3), Rektangel(2, 4), Rektangel(2, 4)]
    leilighet = Leilighet(alle_rom)
    leilighet.skriv_areal_leilighet()

main()
    
