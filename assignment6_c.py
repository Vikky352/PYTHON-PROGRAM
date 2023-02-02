l=[]
n=int(input("enter number of term you want: "))
for i in range(n):
    l.append(int(input()))
c=0
for j in l:
    c+=j
print("sum of whole list are:",c)