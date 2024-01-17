
def factor(int):
    factorArr = []
    for i in range(1, int+1):
        if int % i == 0:
            factorArr.append(i)
    return factorArr


def LCM(n1, n2):
    if n1 > n2:
        higher = n1
    else:
        higher = n2

    value = higher
    while True:
        if higher % n1 == 0 and higher % n2 == 0:
            return higher
        else:
            higher = higher+value


# TEST
# print(LCM(48, 36))


def GCD(n1, n2):
    while n1 % n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    gcd = n2

    return gcd
