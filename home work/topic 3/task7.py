'''Write a python program to create a set of ten numbers by taking input from user.
Now traverse set elements.'''
num_set=set()
for i in range(10):
	num=int(input(f"enter number {i+1}:"))
	num_set.add(num)

print("set element")
for num in num_set:
	print(num)