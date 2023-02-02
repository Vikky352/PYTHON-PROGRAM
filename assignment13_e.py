def evenn(n,i=0):
    i+=2
    if n==1:
        return i
    return i+evenn(n-1,i)
n=int(input("Enetr number of term: "))
r=evenn(n)
print("First %d even natural number sum :"%n,r)