# employee class create
class employee:
 def setemp(self,empid,empname,salary):
  self.empid=empid
  self.empname=empname
  self.salary=salary
 def display(self):
  print("EmployeeId Is: ",self.empid)
  print("EmployeeName Is: ",self.empname)
  print("Salary Is: ",self.salary)
a=int(input("Enter id: "))
b=input("Enter Name: ")
c=int(input("Enter Salary: "))
d=employee()
d.setemp(a,b,c)
d.display()