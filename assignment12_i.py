def cube(n,i=1):
    if n==0:
        return
    else:
        print(i,"=",i*i*i)
        i+=1
        cube(n-1,i)
n=int(input("Enetr number of term: "))
print("First %d cube of natural number :"%n)
cube(n)