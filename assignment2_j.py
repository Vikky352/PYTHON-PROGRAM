print("enter marks of five subject:- ")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
t=m1+m2+m3+m4+m5
p=t/5
if p>=60:
    print("result is first division percentge is %d"%p)
elif p>=50:
    print("result is second division percentge is %d"%p)
elif p>=30:
    print("result is third division percentge is %d"%p)
else:
    print("result is fail percentge is %d"%p)