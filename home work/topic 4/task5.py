'''Write a python program to create a function named rev(), in rev() function pass a
string and this function return reverse string.'''
def rev(a):
	return a[::-1]
b=input("enter string : ")
c=rev(b)
print("Original String:",b)
print("Reversed String:",c)