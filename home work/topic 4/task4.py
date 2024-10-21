'''
Write a python program to create a function named substr(), in substr() function
pass a string and substring. If substring is presented in string then return true or
return false.'''
def substr(astr,bstr):
	if bstr in astr:
		return True
	else:
		return False

a=input("enter string : ")
b=input("enter substring you can look : ")
if substr(a,b):
	print(f"The substring '{b}' is present in the string.")
else:
	print(f"The substring '{b}' is not present in the string.")