'''Write a python program to create a dictionary and traverse elements of dictionary
using for loop.'''
stud_no={
	"amit":40,
	"golu":50,
	"santosh":60,
	"harshit":70,
	"vivek":80,
}
for name,score in stud_no.items():
	print(f"{name}: {score}")