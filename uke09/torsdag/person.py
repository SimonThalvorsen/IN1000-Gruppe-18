class Person:
    def __init__(self, navn: str, rolle: str) -> None:
        self._navn = navn
        self._rolle = rolle

    def __str__(self):
        return self._navn
