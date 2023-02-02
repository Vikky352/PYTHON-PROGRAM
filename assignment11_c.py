def prime(n):
    c=2
    print("First %d Prime number are:"%n)
    while n>0:
        d=0
        for i in range(2,c+1//2):
            if c%i==0:
                d+=1
                break
        if d==0:
            print(c,end=' ')
            n-=1
        c+=1
p=int(input("Enter number of term:"))
prime(p)
    
            