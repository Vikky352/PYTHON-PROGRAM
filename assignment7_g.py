s=input("enter string: ")
l=len(s)
r=''
for i in range(l-1,-1,-1):
    r+=s[i]
if s==r:
    print("string is palindrome",s)
else:
    print("string is not palindrome",s)