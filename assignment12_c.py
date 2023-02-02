def even(n,i=2):
    if n==0:
        return
    else:
        print(i)
        i+=2
        even(n-1,i)
n=int(input("Enetr number of term: "))
print("First %d even natural number are:"%n)
even(n)