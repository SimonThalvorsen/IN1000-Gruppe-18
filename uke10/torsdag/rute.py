class Rute:
    def __init__(self) -> None:
        self._spiller = None

    def plasser_brikke(self, spiller):
        self._spiller = spiller

    def er_opptatt(self):
        if self._spiller is not None:
            return True
        else:
            return False
        
    def hent_brikkeeier(self):
        return self._spiller
    

