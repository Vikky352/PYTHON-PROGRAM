def np(p):
    p+=1
    while True:
        c=0
        for i in range(2,9):
            if p%i==0:
                c+=1 
        if c==0:
            return p
        p+=1        
p=int(input("Enter prime number: "))
r=np(p)
print("Next prime number is :",r)
    