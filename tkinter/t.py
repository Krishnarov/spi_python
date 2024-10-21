from tkinter import*
import time
import sys
win=Tk()
win.title("Status")
win.geometry("500x500")
win.resizable(False,False)

def get_time():
	tim=time.strftime("%I:%M:%S %p")
	clo.config(text=tim)
	clo.after(200,get_time)
def sen_tim():
	h=int(n4.get())
	m=int(n5.get())
	lbl7.config(text=(h," : ",m))
	lbl7.after(200,sen_tim)

fram=Frame(win,bg="#fff",bd=6,relief=RIDGE)
fram.place(x=50,y=50,width=250,height=380)
title=Label(fram,text="Status",font=("goudy old style",20),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)
fram3=Frame(fram,bg="green",bd=2,relief=RIDGE)
fram3.place(x=30,y=80,width=180,height=250)
lbl5=Label(fram3,text="Time",font=("times now roman",25,"bold"),fg="black",bg="green")
lbl5.place(x=50,y=10)

lbl6=Label(fram3,text="Sanding Time",font=("times now roman",24,"bold"),fg="black",bg="green")
lbl6.place(x=10,y=85)

lbl7=Label(fram3,text="",font=("times now roman",26,"bold"),fg="black",bg="green")
lbl7.place(x=10,y=120)

clo=Label(fram3,font=("times now roman",26,"bold"),bg="green",fg="white")
clo.place(x=10,y=50)
get_time()




win.mainloop()