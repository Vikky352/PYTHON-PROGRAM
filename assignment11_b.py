def bin(a):
    p=1
    r=0
    s=''
    while a>0:
        t=a%2
        r+=t*p
        p*=10
        a=a//2
    while r>0:
        t=r%10
        s=s+str(t)
        r//=10     
    print(s)
d=int(input("Enter a decimal number:"))
bin(d)