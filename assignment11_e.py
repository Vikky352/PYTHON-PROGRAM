def dif(n):
    e=0
    o=0
    for i in n:
        if i%2==0:
            e+=1
        else:
            o+=1
    return e,o
            
l=int(input("Enter number of term you want to add: "))
p=[]
print("Enter %d number in list :"%l)
for i in range(l):
    p.append(int(input()))
e,o=dif(p)
print("Total number of even:",e,"\nTotal number of odd:",o)