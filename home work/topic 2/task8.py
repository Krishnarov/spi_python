#Write a python program to find factorial of given number.
n=int(input("Enter number witch you want to factorial "))
fact=1
if n<0:
	print("factorial does not exist for negative number")
elif n==0:
	print("The factorial of 0 is 1 ")
else:
	for i in range(1,n+1):
		fact=fact*i
	print("the factorial of ",n,"is",fact)