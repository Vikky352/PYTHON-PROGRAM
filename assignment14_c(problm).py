class employ:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def sal_sort(s):
        s.sort(key=lambda e:e.salary,reverse=True)
    def name(s):
        s.sort(key=lambda e:e.name)
n=int(input("Enter number of data want to input: "))
s=[]
for i in range(n):
    e=employ(int(input("enter empid:")),input("enter name:"),int(input("Enter salary:")))
    s.append(e)
employ.sal_sort(s)
print("sorted according to name:")
for i in s:
    print(f"{i.empid}->{i.name}:{i.salary}")
employ.name(s)
print("sorted according to salary:")
for i in s:
    print(f"{i.empid}->{i.name}:{i.salary}")
