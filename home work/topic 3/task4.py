'''Write a python program to create a list of five students by taking input from user.
Now display name of students in ascending and descending order.'''
stud=[]
for i in range(5):
	name=input(f"Enter students name {i+1}:")
	stud.append(name)
print("Student names in ascending order:")
for name in sorted(stud):
	print(name)
print("Student names in deascending order:")
for name in sorted(stud,reverse=True):
	print(name)

