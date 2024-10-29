class Spiller:
    def __init__(self, symbol: str) -> None:
        if symbol not in ["X", "O"]:
            print("Ugyldig symbol")
            self._symbol = input("skriv inn rikig symbol: ")
        else:
            self._symbol = symbol

    def __str__(self) -> str:
        return self._symbol



    