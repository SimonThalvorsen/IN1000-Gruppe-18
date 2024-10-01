def tell_grader(fag, bsc, msc):
    return (fag == bsc) + (fag == msc)

def tell_grade2r(fag, bsc, msc):
    sum = 0
    if fag == bsc:
        sum += 1
    if fag == msc:
        sum += 1
    return sum

def hovedprogram():
    x = tell_grader("informatikk", "informatikk", "informatikk")
    print(x)
    x = tell_grader("historie", "informatikk", "informatikk")
    print(x)

hovedprogram()
