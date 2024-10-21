from tkinter import*
root=Tk()
def add():
	a=int(n1.get())
	b=int(n2.get())
	c=a+b
	lbl3.config(text=c)
def sub():
	a=int(n1.get())
	b=int(n2.get())
	c=a-b
	lbl3.config(text=c)
def mul():
	a=int(n1.get())
	b=int(n2.get())
	c=a*b
	lbl3.config(text=c)
def div():
	a=int(n1.get())
	b=int(n2.get())
	c=a/b
	lbl3.config(text=c)

root.geometry("500x500")
f1=Frame(root,bg="#2b289e",height=500,width=250)
f1.place(x=0,y=0)
f2=Frame(root,bg="black",height=500,width=250)
f2.place(x=250,y=0)

f3=Frame(root,bg="gold",height=150,width=250)
f3.place(x=100,y=200)

lbl1=Label(f1,text="Enter frist no",font=("arial 20 bold"))
lbl1.place(x=20,y=100)

lbl2=Label(f1,text="Enter second no",font=("arial 20 bold"))
lbl2.place(x=20,y=150)

lbl3=Label(f3,text="Result",bg="gold",font=("arial 30 bold"))
lbl3.place(x=60,y=50)

n1=Entry(f2,font=("arial 18 bold"),fg="black",width="18")
n1.place(x=20,y=100)
n2=Entry(f2,font=("arial 18 bold"),fg="black",width="18")
n2.place(x=20,y=150)

btn1=Button(f1,text="ADD",fg="red",font=("arial 16 bold"),command=add)
btn1.place(x=20,y=420)
btn1=Button(f1,text="SUB",fg="red",font=("arial 16 bold"),command=sub)
btn1.place(x=120,y=420)
btn1=Button(f2,text="MUL",fg="red",font=("arial 16 bold"),command=mul)
btn1.place(x=20,y=420)
btn1=Button(f2,text="DIV",fg="red",font=("arial 16 bold"),command=div)
btn1.place(x=120,y=420)

root.mainloop()