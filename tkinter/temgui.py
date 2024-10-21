from tkinter import*
def ctof():	
	c=float(n1.get())
	f=(c*9/5)+32	
	res.config(text=(f))
def ftoc():
	f=float(n1.get())
	c=(f-32)*5/9
	res.config(text=(c))



root=Tk()
root.config(bg="azure3")
root.title("temperature converter")
root.geometry("500x500+500+200")
nam=Label(root,text="Temperature Converter",fg="darkblue",font=("Arial 25 bold"))
nam.place(x=100,y=50)
n1=Entry(root,font=("Arial 15 "))
n1.place(x=150,y=125)
res=Label(root,fg="black",font=("Arial 25 bold"))
res.place(x=200,y=200)
ctof=Button(root,text="CTOF",font=("Arial 15"),fg="green",command=ctof)
ctof.place(x=100,y=300)
ftoc=Button(root,text="FTOC",font=("Arial 15"),fg="red",command=ftoc)
ftoc.place(x=300,y=300)
root.mainloop()