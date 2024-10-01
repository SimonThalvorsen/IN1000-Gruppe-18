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
    talllister = []
    for talliste in talllister:
        if er_sortert(talliste):
            sortert[str(s_idx)+"s"] = talliste
            s_idx += 1
        else:
            usortert[str(u_idx)+"s"] = talliste
            u_idx += 1
