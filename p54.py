s=input("enter string ")
rs="".join(reversed(s))
print(s)
print(rs)
if s==rs:
	print("string is palindrome")
else:
	print("string is not palindrome")