from tkinter import*
from tkinter.ttk import Combobox
from forex_python.converter import CurrencyRates
root=Tk()
root.title("Currency converter")
root.geometry("500x400+200+200")
root.config(bg="skyblue")

lbl1=Label(root,text="From",bg="skyblue",fg="white",font=("Arial 18 bold"))
lbl1.place(x=70,y=70)

lbl2=Label(root,text="To",bg="skyblue",fg="white",font=("Arial 18 bold"))
lbl2.place(x=300,y=70)
curr_li=["INR","USD","CAD","EUR","DKK"]
var1=StringVar()
var2=StringVar()
tex=StringVar()
def convert():
	f_com=var1.get()
	t_com=var2.get()
	c=CurrencyRates()
	amt=c.convert(from_currency,to_currency,float(n1.get()))
	amount=float("{:.3f}".format(amt))
	tex.set(amount)

def reset():
	n1.delete(0,END)


f_com=Combobox(root,variable=var1,values=curr_li,font="arial 20",width=10)
f_com.place(x=70,y=100)
f_com.set("IND")

t_com=Combobox(root,variable=var2,values=curr_li,font="arial 20",width=10)
t_com.place(x=300,y=100)
t_com.set("USD")

n1=Entry(root,font=("Arial 20 bold"))
n1.place(x=110,y=150)

btn=Button(root,command=convert(),text="Convert",font=("Arial 22 bold"),fg="blue")
btn.place(x=100,y=200)
btn1=Button(root,command=reset(),text="Reset",font=("Arial 22 bold"),fg="blue")
btn1.place(x=300,y=200)

lbl3=Label(root,textvariable=tex,bg="skyblue",fg="white",font=("Arial 25 bold"))
lbl3.place(x=200,y=280)


root.mainloop()