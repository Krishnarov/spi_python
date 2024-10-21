# create class retangle 
class retangle:
 def __init__(self,l,w ):
  self.l=l
  self.w=w
 def area(self):
  return self.l*self.w
x=int(input("Enter Length: "))
y=int(input("Enter Width: "))
d=retangle(x,y)
print(d.area())