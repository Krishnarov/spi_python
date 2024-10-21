class employee():
 def setvalue(self,emplid,emplname,selary):
  self.emplid=emplid
  self.emplname=emplname
  self.selary=selary
 def display(self):
  print("Employee id ",self.emplid)
  print("Employee name ",self.emplname)
  print("Employee selary ",self.selary)

e=employee()
id=int(input("enter id"))
name=input("enter name")
sal=int(input("enter selary"))
e.setvalue(id,name,sal)
e.display()
