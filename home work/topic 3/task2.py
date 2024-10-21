'''Write a python program to create a list of ten numbers by taking input from user.
Now check a number is presented in list or not.'''
num_list=[]
for i in range(10):
	num=int(input(f"enter number {i+1}: "))
	num_list.append(num)
check_num=int(input("einter number if you to chack in list "))
if check_num in num_list:
	print(check_num,"number is present in the list")
else:
	print(check_num,"number is not present in the list")
