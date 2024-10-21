#Write a python program to find factorial of given number using ‘Recursion’.
def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)
num=int(input("enter number"))
if num<0:
	print("Factorial is not defined for negative numbers")
else:
	res=factorial(num)
	print("The Factorial is ",num,"is",res)