'''Write a python program to create a function search(), in search function pass two
parameters first, a list of ten numbers and second, a number to search. If number is
present in list return index of list otherwise return false.'''
def search(num_list,target):
	if target in num_list:
		return num_list.index(target)
	else:
		return False

num=[]
num_elem=int(input("enter  number of element "))
for i in range(num_elem):
	num1=int(input(f"enter number if you cal enterin list {i+1}: :"))
	num.append(num1)

ser_num=int(input("enter you can search the number : "))
res=search(num, ser_num)
if res is not False:
	print(f"Number {ser_num} found at index {res}")
else:
	print(f"The number {ser_num} is not in the list.")