def nod(n, m):
    if n < 0 or m < 0:
        raise Exception("n and m must be > 0!")
    if not isinstance(n, int) or not isinstance(m, int):
        raise Exception("n and m must be integer!")
    r = n
    while r > 0:
        r = n % m
        n = m
        m = r
    return n + m


def nok(n, m):
    return n*m / nod(n,m)

def gcd():
    pass

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(nok(a,b))
