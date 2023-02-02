def natural(n):
    if n==1:
        return 1
    return n+natural(n-1)
n=int(input("Enetr number of term: "))
s=natural(n)
print("First %d natural number sum:"%n,s)