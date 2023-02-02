def revevn(n):
    if n==0:
        return
    else:
        print(2*n)
        revevn(n-1)
n=int(input("Enetr number of term: "))
print("First %d even natural number in reverse order:"%n)
revevn(n)