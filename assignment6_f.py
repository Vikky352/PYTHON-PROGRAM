l=[]
n=int(input("enter number of term you want: "))
for i in range(n):
    l.append(int(input()))
    
print("Number  index")
for i in l:
    print(" ",i,"->",l.index(i))
    