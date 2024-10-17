from person import Person


class Episode:
    def __init__(self, tittel: str, nummer: int) -> None:
        self._tittel = tittel
        self._nummer = nummer
        self._gjester = []
        self._host = None

    def legg_til_host(self, navn):
        if self._host is None:
            host = Person(navn, "Host")
            self._host = host

    def legg_til_gjest(self, navn):
        gjest = Person(navn, "Gjest")
        self._gjester.append(gjest)

    def __str__(self):
        ut_string = ""
        ut_string += self._tittel + " " + str(self._nummer) + "\n"
        ut_string += "Host: " + str(self._host) + "\n"
        ut_string += "Gjest:\n"
        for gjest in self._gjester:
            ut_string += str(gjest) + "\n"
        return ut_string
