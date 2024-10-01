def tell_grader(fag, bsc, msc):
    return (fag == bsc) + (fag == msc)


def hovedprogram():
    x = tell_grader("informatikk", "informatikk", "informatikk")
    print(x)
    x = tell_grader("historie", "informatikk", "informatikk")
    print(x)

hovedprogram()
