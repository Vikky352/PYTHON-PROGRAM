t=eval(input("enter values to tuple: "))
for i in range(len(t)-1,-1,-1):
    print(t[i],end=' ')
    
# this will reverse with slice function return in tuple   
# print("reverse of tuple :",t[len(t)-1::-1])