n=int(input("enter number: "))
for i in range(1,7):
    for j in range(1,7):
        if i+j==n:
            print("The first dice value will be %d and second dice value will be %d"%(i,j))