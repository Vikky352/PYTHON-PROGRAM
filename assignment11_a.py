def lcm(a,b):
    if a>b:
        max=a
    else:
        max=b
    while True:
        if max % a==0 and max % b==0:
            lcm=max
            break
        max+=1
    return lcm
a,b=[int(x) for x in input("Enetr number:").split(',')]
x=lcm(a,b)
print("Lcm of two number is :",x)

