import tempconv
def main():
	temp=int(input("enter celsius value "))
	a=tempconv.ctof("enter value ",temp)
	print(temp,f"Celsius is equal to {a:.2f} fahrenheit")

	temp1=float(input("enter fahrenheit value "))
	b=tempconv.ftoc("enter value",temp1)
	print(temp1,f"Fahrenheit is equal to {b:.2f} celsius")

main()
