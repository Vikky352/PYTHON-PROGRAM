def oddn(n,i=1):
    if n==1:
        return 1
    i+=2
    return i+oddn(n-1,i)
n=int(input("Enetr number of term: "))
r=oddn(n)
print("First %d odd natural number sum :"%n,r)