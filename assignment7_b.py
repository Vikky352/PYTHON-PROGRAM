s=input("enter string: ")
l=len(s)
c=0
for i in range(l):
    if s[i]=='a'or s[i]=='e'or s[i]=='i'or s[i]=='o'or s[i]=='u':
        c+=1
    elif s[i]=='A'or s[i]=='E'or s[i]=='I'or s[i]=='O'or s[i]=='U':
        c+=1
print("number of vowels in string is:",c)