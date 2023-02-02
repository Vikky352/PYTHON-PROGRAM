t=eval(input("Enter tuple values: "))
c=0
for i in range(len(t)):
    if c<t[i]:
        c=t[i]
print("Maximum value in tuple:",c)

# this will return max with max function
# print("Maximum value in tuple:",max(t))