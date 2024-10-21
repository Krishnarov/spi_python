from tkinter import*
from tkinter import messagebox
import pywhatkit
import pyautogui
import time
import sys


root=Tk()
root.title("whatsaap")
root.geometry("900x500")
root.resizable(False,False)
def get_time():
	tim=time.strftime("%H:%M:%S")
	clo.config(text=tim)
	clo.after(200,get_time)

def send():
	pon=int(n2.get())
	msg=n1.get(1.0,"end-1c")
	nom=int(n3.get())
	hou=int(n4.get())
	mun=int(n5.get())

	def new():
		win=Tk()
		win.title("Status")
		lal=Label(win,text="Message Sending Succcessful..",font=("times now roman",26,"bold"),fg="black",bg="green")
		lal.pack()
		win.mainloop()

	if msg!="" and pon!="" and nom!="" and hou!="" and mun!="":
		try:
			pywhatkit.sendwhatmsg('+91'+str(pon), msg, hou, mun)
			time.sleep(1)
			i=0
			while i<nom:
				pyautogui.typewrite(msg)
				pyautogui.press('enter')
				i=i+1
			pr=print("Message Sent!")
			new()
		except:
			messagebox.showerror("Error in sending the message")

	else:
		messagebox.showwarning("Invalid","plesse enter value")

def stop():
	root.destroy()


title=Label(root,text="Whatsaap",font=("times now roman",40),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)
fram=Frame(root,bg="#fff",bd=6,relief=RIDGE)
fram.place(x=50,y=100,width=500,height=380)
title1=Label(fram,text="Details",font=("goudy old style",20),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)

lbl1=Label(fram,text="Enter msg :",font=("times now roman",18,"bold"),bg="#fff",fg="black").place(x=20,y=75)
lbl2=Label(fram,text="Enter mobile no :",font=("times now roman",18,"bold"),bg="#fff",fg="black").place(x=20,y=150)
lbl3=Label(fram,text="Numbers of msg :",font=("times now roman",18,"bold"),bg="#fff",fg="black").place(x=20,y=200)
lbl4=Label(fram,text="Time :",font=("times now roman",18,"bold"),bg="#fff",fg="black").place(x=20,y=250)
my=Label(fram,text="developed by :-",font=("times now roman",10),bg="#fff",fg="black").place(x=300,y=340)
my_n=Label(fram,text=" Er. Krishna Kumar",font=("times now roman",10,"bold"),bg="#fff",fg="black").place(x=380,y=340)

n1=Text(fram,font=("times now roman",15,"bold"),bg="lightyellow",fg="black")
n1.place(x=200,y=50,height=80,width=250)

n2=Entry(fram,font=("times now roman",15,"bold"),bg="lightyellow",fg="black")
n2.place(x=200,y=150,width=250)
n3=Entry(fram,font=("times now roman",15,"bold"),bg="lightyellow",fg="black")
n3.place(x=200,y=200,width=250)
n4=Entry(fram,font=("times now roman",15,"bold"),bg="lightyellow",fg="black")
n4.place(x=200,y=250,width=120)
n5=Entry(fram,font=("times now roman",15,"bold"),bg="lightyellow",fg="black")
n5.place(x=330,y=250,width=120)
btn=Button(fram,text="Exit",font=("times now roman",18,"bold"),fg="black",bg="green",command=stop).place(x=50,y=300,width=100,height=30)
btn1=Button(fram,text="Send",font=("times now roman",18,"bold"),fg="black",bg="green",command=send).place(x=200,y=300,width=100,height=30)
btn2=Button(fram,text="Clear",font=("times now roman",18,"bold"),fg="black",bg="green").place(x=350,y=300,width=100,height=30)
fram1=Frame(root,bg="#fff",bd=6,relief=RIDGE)
fram1.place(x=600,y=100,width=250,height=380)
title2=Label(fram1,text="Status",font=("goudy old style",20),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)
fram3=Frame(fram1,bg="green",bd=2,relief=RIDGE)
fram3.place(x=35,y=80,width=180,height=250)
lbl5=Label(fram3,text="Time",font=("times now roman",25,"bold"),fg="black",bg="green")
lbl5.place(x=50,y=10)
lbl7=Label(fram3,text="",font=("times now roman",25,"bold"),fg="black",bg="green")
lbl7.place(x=10,y=120)
clo=Label(fram3,font=("times now roman",28,"bold"),bg="green",fg="white")
clo.place(x=20,y=50)
get_time()


root.mainloop()

