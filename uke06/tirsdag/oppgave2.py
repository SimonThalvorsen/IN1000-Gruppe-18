def forkort_lagliste(lagliste):
    return list(set(lagliste))


def hovedprogram():
    lagliste = ["Molde", "Brann", "Molde"]
    print(forkort_lagliste(lagliste))

hovedprogram()
