class Person:
    def __init__(self, navn, fodeselsaar):
        self._navn = navn
        self._alder = 2024 - fodeselsaar
        if self._alder == 0:
            self._er_baby = True
        else:
            self._er_baby = False

        self._venner = []
        
        
    def er_baby(self):
        return self._er_baby

    def hent_navn(self):
        return self._navn
    
    def endre_navn(self, nytt_navn):
        self._navn = nytt_navn

    def hent_alder(self):
        return self._alder

    def bursdag(self):
        self._alder += 1





