l=[]
n=int(input("enter number of term: "))
for i in range(n):
    l.append(int(input()))
print("before sort list is :",l)

l.sort()
print("After sort list is :",l)