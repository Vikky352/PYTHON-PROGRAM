def odd(n,i=1):
    if n==0:
        return
    else:
        print(i)
        i+=2
        odd(n-1,i)
n=int(input("Enetr number of term: "))
print("First %d odd natural number in :"%n)
odd(n)