#Write a python program to create a list of ten numbers by taking input from user.
list1=[]
n=int(input('enter numbers in list'))
print("enter",n,"elements")
for i in range(n):
	e=eval(input())
	list1.insert(i,e)
print("you have enter following elements")
for e in list1:
	print(e)