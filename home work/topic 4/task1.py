#Write a python program to create two functions area() and peri() to find area and perimeter of rectangle.
def area(l,m):
	return(l*m)
def peri(l,m):
	return(2*(l+m))

a=int(input("enter lantgh"))
b=int(input("enter base "))
print("area is =",area(a,b))
print("perimeter is =",peri(a,b))
