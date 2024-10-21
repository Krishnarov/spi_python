#wap to find volume and surface area of cuboid.

l=float(input("Enter length"))
b=float(input("Enter base "))
h=float(input("Enter height"))
vol=l*b*h
sur=2*(l*b+b*h+h*l)
print("the volume is : ",vol)
print("the surface is : ",sur)