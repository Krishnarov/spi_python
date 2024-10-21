#eh
try:
 a=int(input("enter frist no : "))
 b=int(input("enter second no : "))
 c=a/b
 print("div =",c)
except NameError:
 print("value glath inter hai")
except ZeroDivisionError:
 print("do not input 0")
finally:
 print("thank you")