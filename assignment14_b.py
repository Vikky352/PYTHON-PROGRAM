class employ:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def show(s):
        print("empid=",s.empid,"Name=",s.name,"Salary=",s.salary)

e1=employ(int(input("enter empid:")),input("enter name:"),int(input("Enter salary:")))
e1.show()