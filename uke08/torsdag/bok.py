class Bok:
    def __init__(self, tittel, forfatter, isbn):
        self._tittel = tittel
        self._forfatter = forfatter
        self._isbn = isbn
        self._er_tilgjenglig = True

    def er_tilgjengelig(self):
        return self._er_tilgjenglig
    
    def laan_ut(self):
        self._er_tilgjenglig = False

    def lever_tilbake(self):
        self._er_tilgjenglig = True

    def hent_tittel(self):
        return self._tittel
    
    def hent_forfatter(self):
        return self._forfatter
    
    def hent_isbn(self):
        return self._isbn
    
    def tittel_inneholder(self, str):
        return str.lower() in self._tittel.lower()