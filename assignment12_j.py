def revcube(n):
    if n==0:
        return
    else:
        print(n,"=",n*n*n)
        revcube(n-1)
n=int(input("Enetr number of term: "))
print("First %d natural number cube in reverse order:"%n)
revcube(n)