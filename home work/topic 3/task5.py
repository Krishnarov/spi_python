'''Write a python program to create a tuple of five numbers. Now apply len(), max(),
min() and sum() functions on tuple.'''
num_tuple=tuple(int(input(f"enter number {i+1}:"))for i in range(5))
	
	
a=len(num_tuple)
print("Length of the tuple:",a)
b=max(num_tuple)
print("Maximum value in the tuple:",b)
c=min(num_tuple)
print("Minimum value in the tuple:",c)
d=sum(num_tuple)
print("Sum of values in the tuple:",d)