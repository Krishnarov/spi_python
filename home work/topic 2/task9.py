#Write a python program to find sum of digits of given number.
num=input("enter number ")
sum=0
for i in num:
	sum=sum+int(i)
print(sum)