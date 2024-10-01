def forkort_lagliste(lagliste):
    return list(set(lagliste))


def hovedprogram():
    lagliste = ["Molde", "Brann", "Molde"]
    print(lagliste, forkort_lagliste(lagliste))

hovedprogram()
