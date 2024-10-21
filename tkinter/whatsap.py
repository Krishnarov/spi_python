import pywhatkit
import pyautogui
import time
a=input("enter you massage ")
b=int(input("enter mobil no in "))
d=int(input("enter how mani time send msg "))
e=int(input("enter time in hour "))
c=int(input("enter time in min "))

pywhatkit.sendwhatmsg('+91'+str(b), a, e, c)
time.sleep(5)
i=0
while i<=d:
	pyautogui.typewrite(a+str(i))
	pyautogui.press('enter')
	i=i+1