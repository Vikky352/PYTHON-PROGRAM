t1=eval(input("enter values to tuple: "))
t2=eval(input("enter values to tuple: "))
if set(t1).issubset(t2):
    print("tuple1 is subset of tuple2")
elif set(t2).issubset(t1):
    print("tuple2 is subset of tuple1")
else:
    print("tuple1 is no any  subset of tuple 2")