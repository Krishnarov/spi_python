from tkinter import*
from tkinter import messagebox
import ast
root=Tk()
root.title("SignUp")
root.geometry("925x500+0+100")
root.config(bg="#fff")
root.resizable(False,False)

def sinup():
	username=n1.get()
	password=n2.get()
	c_password=n3.get()
	if password==c_password:
		try:
			file=open("datasheet.txt",'r+')
			d=file.read()
			r=ast.literal_eval(d)

			dict2={username:password}
			r.update(dict2)
			file.truncate(0)
			file.close()

			file=open("datasheet.txt","w")
			w=file.write(str(r))

			messagebox.showinfo('SignUp','sucessfuly sign up')
		except:
			file=open("datasheet.txt",'r+')
			pp=str({"username":"password"})
			file.write(pp)
			file.close()
	else:
		messagebox.showerror("Invalid","Both password should match")

def sign():
	root.destroy()




img=PhotoImage(file="login.png")
Label(root,image=img,border=0,bg="#fff").place(x=50,y=90)

f1=Frame(root,bg='#fff',height=390,width=350)
f1.place(x=480,y=50)

lbl1=Label(f1,text="Sign Up",bg="#fff",fg="blue",font=("Microsoft Yahei UI Light ",23," bold"))
lbl1.place(x=120,y=50)

def on_enter(e):
	n1.delete(0,'end')
def on_leave(e):
	if n1.get()=="":
		n1.insert(0,"Username")

n1 = Entry(f1,width=35,fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
n1.place(x=50,y=100)
n1.insert(0,'Username')
n1.bind('<FocusIn>',on_enter)
n1.bind('<FocusOut>',on_leave)
#n1.pack()

Frame(f1,bg="black",width=250,height=2).place(x=50,y=120)


def on_enter(e):
	n2.delete(0,'end')
def on_leave(e):
	if n2.get()=="":
		n2.insert(0,"Password")

n2 = Entry(f1,width=35,fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
n2.place(x=50,y=150)
n2.insert(0,'Password')
n2.bind('<FocusIn>',on_enter)
n2.bind('<FocusOut>',on_leave)
#n1.pack()

Frame(f1,bg="black",width=250,height=2).place(x=50,y=170)

def on_enter(e):
	n3.delete(0,'end')
def on_leave(e):
	if n3.get()=="":
		n3.insert(0,"Conform Password")

n3 = Entry(f1,width=35,fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
n3.place(x=50,y=200)
n3.insert(0,'Conform Password')
n3.bind('<FocusIn>',on_enter)
n3.bind('<FocusOut>',on_leave)
#n1.pack()

Frame(f1,bg="black",width=250,height=2).place(x=50,y=220)


Button(f1,width=20,pady=7,text="Sign Up",bg='#57a1f8',fg='white',border=0,command=sinup).place(x=60,y=250)
lbl2=Label(f1,text="I have an acount",bg="#fff",fg="black",font=("Microsoft Yahei UI Light ",9))
lbl2.place(x=70,y=300)
btn=Button(f1,width=6,text="Sign in",highlightbackground="white",highlightthickness=-1,border=0,bg="white",fg="#57a1f8",cursor="hand1",command=sign)
btn.place(x=150,y=300)

root.mainloop()