def digit(n):
    if n==0:
        return 0
    r=n%10
    return r+digit(n//10)
n=int(input("Enetr number of term: "))
r=digit(n)
print("%d of digit sum :"%n,r)
    