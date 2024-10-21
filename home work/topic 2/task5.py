#Write a python program to compute gross salary based on following parameters:-
salary=float(input("enter basic salary "))
if (salary==1,4000):
	a=float(salary*0.10)
	b=float(salary*0.50)
	l=salary+a+b
	print("basic salary is ",salary)
	print("dearness allow is :",b)
	print("house rent allow is :",a)
	print("all about salary is :",l)
elif(salary==4001,8000):
	c=float(salary*0.15)
	d=float(salary*0.60)
	m=salary+c+d
	print("basic salary is ",salary)
	print("dearness allow is :",d)
	print("house rent allow is :",c)
	print("all about salary is :",m)
elif(salary==8001,12000):
	e=float(salary*0.20)
	f=float(salary*0.70)
	n=salary+e+f
	print("basic salary is ",salary)
	print("dearness allow is :",f)
	print("house rent allow is :",e)
	print("all about salary is :",n)
elif(salary==12000<100000):
	g=float(salary*0.25)
	h=float(salary*0.80)
	o=salary+g+h
	print("basic salary is ",salary)
	print("dearness allow is :",h)
	print("house rent allow is :",g)
	print("all about salary is :",o)
