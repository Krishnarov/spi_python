a=input("enter your name : ")
#print(a)
sn=a.split(" ")
#print(sn)
print("your short name ",end="")
for i in range(len(sn)-1):
	print(sn[i][0]+".",end="")
print(sn[len(sn)-1])