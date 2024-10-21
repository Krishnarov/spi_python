#grater
def greatest(x,y,z):
 if x>y and x>z:
  return(x)
 elif y>z and y>z:
  return(y)
 else:
  return(z)

a=int(input("frist no "))
b=int(input("second no "))
c=int(input ("last no "))
print(greatest(a,b,c))