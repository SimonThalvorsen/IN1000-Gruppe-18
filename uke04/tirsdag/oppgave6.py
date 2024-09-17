# Her bruker jeg argumenter og returverdier for å enklere teste, dette er ikke pensum før onsdagens forelsening.
# Selve logikken (de to while-løkkene) er essensen av koden.
def fjern_null(liste):
    while liste and liste[0] == 0:
        liste.pop(0)
    while liste and liste[-1] == 0:
        liste.pop()
    return liste




assert fjern_null([0, 0, 0, 0, 0]) == []
assert fjern_null([0]) == []
assert fjern_null([5]) == [5]
assert fjern_null([0, 0, 1, 2, 3]) == [1, 2, 3]
assert fjern_null([1, 0, 2, 0, 3]) == [1, 0, 2, 0, 3]
assert fjern_null([0, 0, 1, 2, 0, 3, 0, 0, 4, 0]) == [1, 2, 0, 3, 0, 0,4]




