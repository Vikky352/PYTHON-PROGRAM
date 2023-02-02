s=input("enter string: ")
l=len(s)
p=''
for i in range(l-1,-1 ,-1):
    p=p+s[i]
print("resverse of string:",p)
# reverse string using slicing function
# print(p[l-1::-1])