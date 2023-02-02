def sqr(n,i=1):
    if n==0:
        return
    else:
        print(i,"=",i*i)
        i+=1
        sqr(n-1,i)
n=int(input("Enetr number of term: "))
print("First %d Square of natural number :"%n)
sqr(n)