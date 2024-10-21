class cal():
	def add(self,x,y):
		return(x+y)
	def sub(self,x,y):
		return(x-y)
	def mul(self,x,y):
		return(x*y)
	def div(self,x,y):
		return(x/y)
a=int(input("enter frist no "))
b=int(input("enter second no "))
c=cal()
d=c.add(a,b)
e=c.sub(a,b)
f=c.mul(a,b)
g=c.div(a,b)
print("add is =",d)
print("sub is =",e)
print("mul is =",f)
print("div is =",g)
