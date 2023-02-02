def revsqr(n):
    if n==0:
        return
    else:
        print(n,"=",n*n)
        revsqr(n-1)
n=int(input("Enetr number of term: "))
print("First %d natural number square in reverse order:"%n)
revsqr(n)