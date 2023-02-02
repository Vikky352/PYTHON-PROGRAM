l=int(input("Enetr number of item "))
d={}
for i in range(1,l+1):
    print("Enetr value for key",i)
    d[i]=int(input())
c=0
for i in range(1,l+1):
    c=c+d[i]
print("Sum of values of dictionary will be:",c)