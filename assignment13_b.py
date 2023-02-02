def sqr(n):
    if n==1:
        return 1
    return n*n + sqr(n-1)
n=int(input("Enetr number of term: "))
r=sqr(n)
print("First %d natural number square sum :"%n,r)