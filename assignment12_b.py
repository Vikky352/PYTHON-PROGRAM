def revnat(n):
    if n==1:
        print(n)
        return
    else:
        print(n)
        revnat(n-1)
n=int(input("Enetr number of term: "))
print("First %d natural number in reverse order:"%n)
revnat(n)