import random

def er_sortert(talliste: list[int]):
    forrige = talliste[0]
    for tall in talliste:
        if not forrige <= tall:
            return False
        forrige = tall
    return True

def hovedprogram():
    sortert = {}
    usortert = {}

    s_idx = 1
    u_idx = 1
    
    # Prøve gjerne å forstå hva som skjer her, men det er ABSOLUTT ikke forventet kode dere skal kunne i IN1000
    # Det den gjør er å generere en liste av lister, hvor ~50% er sorterte. Alle listene har variabel størrelse osv.
    talllister = [
    sorted([random.randint(1, 50) for _ in range(random.randint(5, 15))]) if random.choice([0, 1])
    else [random.randint(1, 50) for _ in range(random.randint(5, 15))]
    for _ in range(random.randint(1, 15))
    ]

    for talliste in talllister:
        if er_sortert(talliste):
            sortert[str(s_idx)+"s"] = talliste
            s_idx += 1
        else:
            usortert[str(u_idx)+"s"] = talliste
            u_idx += 1
    print("sorterte_lister:")
    for value in sortert.values():
        print(value)
    
    print("\nusorterte_lister:")
    for value in usortert.values():
        print(value)

hovedprogram()
