def kalkuler_utgifter(filnavn):
    tot_utgift = 0
    for line in open(filnavn):
        utgift = int(line)
        tot_utgift += utgift

def hovedprogram():
    fn_peter = "Peter.txt"
    print("Peter har brukt: ", kalkuler_utgifter(fn_peter))

    fn_paul = "Paul.txt"
    print("Paul har brukt: ", kalkuler_utgifter(fn_paul))

hovedprogram()
