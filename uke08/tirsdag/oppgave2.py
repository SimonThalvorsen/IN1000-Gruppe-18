class Gruppe:
    def __init__(self, gruppe_nr):
        self._gruppe_nr = gruppe_nr
        self._oppmote = 0

    def hent_oppmote(self):
        return self._oppmote

    def hent_gruppe_nr(self):
        return self._gruppe_nr

    def legg_til_oppmote(self, oppmote):
        self._oppmote += oppmote

def main():
    fil = open("oppmøte_in1000.txt", "r")
    gruppe_nr_liste = fil.readline().strip().split(";")
    grupper = []
    for gruppe_nr in gruppe_nr_liste:
        grupper.append(Gruppe(gruppe_nr))

    for linje in fil:
        oppmote = linje.strip().split(";")
        for i in range(len(grupper)):
            ant_oppmotte = oppmote[i]
            grupper[i].legg_til_oppmote(int(ant_oppmotte))
    fil.close()
       
    for gruppe in grupper:
        print(gruppe.hent_gruppe_nr(), gruppe.hent_oppmote())





main()
