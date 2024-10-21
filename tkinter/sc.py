from tkinter import *
def add():
	a=int(n1.get())
	b=int(n2.get())
	c=a+b
	res.config(text=(c))
def sub():
	a=int(n1.get())
	b=int(n2.get())
	c=a-b
	res.config(text=(c))
def mul():
	a=int(n1.get())
	b=int(n2.get())
	c=a*b
	res.config(text=(c))
def div():
	a=int(n1.get())
	b=int(n2.get())
	c=a/b
	res.config(text=(c))



root=Tk()
root.title("simple calculator")
root.geometry("500x500+500+200")
lbl=Label(root,text="Simple Calculator",fg="blue",font=("Arial 20 bold"))
lbl.place(x=170,y=50)
lbl1=Label(root,text="Enter frist no :",fg="black",font=("Arial 15 "))
lbl1.place(x=50,y=100)
n1=Entry(root,font=("Arial 15"))
n1.place(x=170,y=100)
lbl2=Label(root,text="Enter second no :",fg="black",font=("Arial 15"))
lbl2.place(x=50,y=150)
n2=Entry(root,font="Arial 15")
n2.place(x=170,y=150)
res=Label(root,text=" ",fg="black",font=("Arial 20 bold"))
res.place(x=200,y=200)
btnadd=Button(root,text="ADD",font=("Arial 15 "),fg="blue",command=add)
btnadd.place(x=100,y=250)
btnsub=Button(root,text="SUB",font=("Arial 15"),fg="red",command=sub)
btnsub.place(x=170,y=250)
btnmul=Button(root,text="MUL",font=("Arial 15"),fg="yellow",command=mul)
btnmul.place(x=250,y=250)
btndiv=Button(root,text="DIV",font=("Arial 15"),fg="green",command=div)
btndiv.place(x=320,y=250)
root.mainloop()