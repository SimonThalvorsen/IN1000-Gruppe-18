from rute import Rute
from spiller import Spiller

class Brett:
    def __init__(self) -> None:
        self._brett = []
        for rad in range(3):
            tmp = []
            for kol in range(3):
                tmp.append(Rute())
            self._brett.append(tmp)
        
        self._p1 = None
        self._p2 = None

    def legg_til_spiller(self, symbol):
        player = Spiller(symbol)
        if self._p1 is None:
            self._p1 = player
        elif self._p2 is None:
            self._p2 = player
        else:
            print("Maks 2 spillere per runde!!")


    def plasser_brikke(self, spiller, x, y):
        if x in [1, 2, 3] and y in [1, 2, 3]:
            rute = self._brett[y-1][x-1]
            if not rute.er_opptatt():
                rute.plasser_brikke(spiller)
            else:
                print("Ikke ledig rute")
        else:
            print("ikke gyldig koordinat")

    
    def sjekk_vinner(self):
        for rad in self._brett:
            if rad[0].hent_eier() == rad[1].hent_eier() and rad[1].hent_eier() is rad[2].hent_eier():
                return rad[0].hent_eier()
            
        for i in range(3):
            tmp = []
            for rad in self._brett:
                tmp.append(rad[i].hent_eier())
            if tmp[0] == tmp[1] == tmp[2]:
                return tmp[0]
            
        if self.brett[0][0] is not None and self.brett[0][0] == self.brett[1][1] == self.brett[2][2]:
            return self.brett[0][0]

        if self.brett[0][2] is not None and self.brett[0][2] == self.brett[1][1] == self.brett[2][0]:
            return self.brett[0][2]
            
        return None
            
            
        



