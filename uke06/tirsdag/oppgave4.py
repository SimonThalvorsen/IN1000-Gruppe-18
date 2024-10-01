# Her bruker jeg noe som heter typehinting, det gjør ingenting for koden
# men gjør det lettere for bruker å se hva slagt type parametrene har
def fjern_vokeler(streng: str, vokaler:list[str]):
    ut_streng = ""
    for char in streng:
        if char in vokaler:
            continue
        else:
            ut_streng += char
    return ut_streng


def fjern_vokeler2(streng: str, vokaler:list[str]):
    ut_streng = []
    for char in streng:
        if char not in vokaler:
            ut_streng.append(char)
            
    return "".join(ut_streng)


def hovedprogram():
    streng = "ha det fint"
    vokaler = ['a', 'e', 'i', 'o', 'u', 'y']

    print(fjern_vokeler(streng, vokaler))
    print(fjern_vokeler2(streng, vokaler))

hovedprogram()
