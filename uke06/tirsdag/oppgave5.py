def er_sortert(talliste: list[int]):
    forrige = talliste[0]
    for tall in talliste:
        if not forrige <= tall:
            return False
        forrige = tall
    return True

def hovedprogram():
    print(er_sortert([2, 4, 6, 8, 10, 12]))
    print(er_sortert([4, 4, 4, 4, 6, 8, 10, 12]))
    print(er_sortert([4, 4, 4, 2, 6, 8, 10, 12]))

hovedprogram()
