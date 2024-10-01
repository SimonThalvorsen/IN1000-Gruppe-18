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


    # fn_peter = "Peter.txt"
    # tot_peter = 0
    #
    # for line in open(fn_peter):
    #     utgift_peter = int(line)
    #     tot_peter += utgift_peter
    #     print("Peter har brukt: ", tot_peter)
    #
    #
    # fn_paul = "Paul.txt"
    # tot_paul = 0
    # for line in open(fn_paul):
    #     utgift_paul = int(line)
    #     tot_paul += utgift_paul
    #     print("Paul har brukt: ", tot_paul)
hovedprogram()
