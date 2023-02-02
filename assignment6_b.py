l=[]
n=int(input("enter number of term: "))
for i in range(n):
    l.append(int(input()))
c=0
for k in l:
    if k>c:
        c=k
print("largest element in list is :",c)
    