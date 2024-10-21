#Write a python program to find roots of quadratic equation ax 2 +bx+c=0.
import math
a=int(input("enter frist no "))
b=int(input("enter second no "))
c=int(input("enter therd no "))
root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
print("the solution are {0} and {1} ".format(root1,root2))