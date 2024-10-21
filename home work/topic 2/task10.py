# Write a python program to reverse the digits of given number.
num=int(input("enter a number "))
reve=0
while num>0:
	rem=num%10
	reve=reve*10+rem
	num//=10
print("reversed number : ",reve)