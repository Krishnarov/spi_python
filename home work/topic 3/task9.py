'''Write a python program to create a dictionary by taking input from user. Now
traverse elements of dictionary.'''
dicti={}
elem_num=int(input("enter number  of elements"))
for i in range(elem_num):
	key=int(input(f"enter key {i+1}:"))
	value=int(input(f"enter value {key}:"))
	dicti[key]=value

for key,value in dicti.items():
	print(f"{key}: {value}")