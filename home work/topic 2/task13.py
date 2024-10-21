'''Write a python program to print series of prime numbers in given range. Range must be created by taking input from user.'''
lnum=int(input("enter lover numbers : "))
unum=int(input("enter upper numbers : "))
print("prime numbers between ",lnum,'and',unum,"are")
for num in range(lnum,unum+1):
	if num>1:
		for i in range(2,num):
			if (num%i)==0:
				break
		else:
			print(num)