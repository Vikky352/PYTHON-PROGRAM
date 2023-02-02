def revodd(n):
    if n==0:
        return 
    else:
        print(2*n-1)
        revodd(n-1)
n=int(input("Enetr number of term: "))
print("First %d odd natural number in reverse order:"%n)
revodd(n)