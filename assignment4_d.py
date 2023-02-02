f=int(input("Enter starting point :-"))
l=int(input("Enetr ending point:- "))
print("prime number between two number :- ")
while f<=l:
    c=0
    for i in (2,f-1):
        if f%i==0:
            c+=1
    if c==0:
        print(f)
    f+=1