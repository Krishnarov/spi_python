#Write a python program to take coordinates of a point as input and determine its
quadrant.
x=int(input("enter valu X "))
y=int(input("enter valu Y "))
if(x<0 and y>0):
	print("belong to 1st Quadrnt.")
elif(x>0 and y>0):
	print("belong to 2nd Quadrnt.")
elif(x<0 and y<0):
	print("belong to 3rd Quadrnt")
else:
	print("belong to 4th Quadrnt")