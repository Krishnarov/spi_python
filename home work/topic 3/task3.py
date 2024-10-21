'''Write a python program to create a list of ten numbers by taking input from user
named AR. Now copy even numbers in list EAR and odd numbers in list OAR. Now
display elements of EAR and OAR.'''
num_list=[]
even=[]
odd=[]
for i in range(10):
	num=int(input(f"Enter number in list {i+1}: "))
	num_list.append(num)
for num in num_list:
	if num%2==0:
		even.append(num)
	else:
		odd.append(num)
print("all even number is :",even)
print("all odd number is : ",odd)