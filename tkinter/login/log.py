from tkinter import*
from tkinter import messagebox
import ast
root=Tk()
root.title("Login")
root.geometry("925x500+0+100")
root.config(bg="#fff")
root.resizable(False,False)

def signin():
	username=n1.get()
	password=n2.get()

	file=open("datasheet.txt",'r+')
	d=file.read()
	r=ast.literal_eval(d)
	#dict2={username:password}
	file.close()
	#print(r.keys())
	#print(r.values())

	if username in r.keys() and password==r[username]:
		screen=Toplevel(root)
		screen.title("hello")
		screen.geometry("925x500+0+100")
		screen.config(bg="white")

		Label(screen,text="Hello Sir My name is Krishna kumar",bg="white",fg="black",font=("calibri(Body)",40,"bold")).pack(expand=True)

		screen.mainloop()
	else:
		messagebox.showerror("Invalid","Invalid username and password")

def signup():
	window=Toplevel(root)
	window.title("SignUp")
	window.geometry("925x500+0+100")
	window.config(bg="#fff")
	window.resizable(False,False)

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
		window.destroy()




	img=PhotoImage(file="login.png")
	Label(window,image=img,border=0,bg="#fff").place(x=50,y=90,width=500,height=400)

	f1=Frame(window,bg='#fff',height=390,width=350)
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

	n2 = Entry(f1,width=35,show="*",fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
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
	
	n3 = Entry(f1,width=35,show="*",fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
	n3.place(x=50,y=200)
	n3.insert(0,'Conform Password')
	n3.bind('<FocusIn>',on_enter)
	n3.bind('<FocusOut>',on_leave)
	#n1.pack()
	
	Frame(f1,bg="black",width=250,height=2).place(x=50,y=220)
	
	
	Button(f1,width=20,pady=7,text="Sign Up",bg='blue',fg='white',border=0,command=sinup).place(x=60,y=250)
	lbl2=Label(f1,text="I have an acount",bg="#fff",fg="black",font=("Microsoft Yahei UI Light ",9))
	lbl2.place(x=70,y=300)
	btn=Button(f1,width=6,text="Sign in",highlightbackground="white",highlightthickness=-1,border=0,bg="white",fg="#57a1f8",cursor="hand1",command=sign)
	btn.place(x=150,y=300)

	window.mainloop()
#######################################


img=PhotoImage(file="log.png")
Label(root,image=img,border=0,bg="#fff").place(x=50,y=90)
f1=Frame(root,bg='#fff',height=390,width=350)
f1.place(x=480,y=50)
lbl1=Label(f1,text="Log In",bg="#fff",fg="blue",font=("Microsoft Yahei UI Light ",23," bold"))
lbl1.place(x=120,y=50)


def on_enter(e):
	n1.delete(0,'end')
def on_leave(e):
	if n1.get()=="":
		n1.insert(0,"Username")
n1 = Entry(f1,width=35,fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
n1.place(x=50,y=120)
n1.insert(0,'Username')
n1.bind('<FocusIn>',on_enter)
n1.bind('<FocusOut>',on_leave)
#n1.pack()

Frame(f1,bg="black",width=250,height=2).place(x=50,y=140)

def on_enter(e):
	n2.delete(0,'end')
def on_leave(e):
	if n2.get()=="":
		n2.insert(0,"Password")

n2 = Entry(f1,width=35,fg='black',highlightbackground="white",highlightthickness=0,border=0,bg='white',font=('Microsoft Yahei UI Light',11))
n2.place(x=50,y=170)
n2.insert(0,'Password')
#n2.config(show="*")
n2.bind('<FocusIn>',on_enter)
n2.bind('<FocusOut>',on_leave)
#n1.pack(show="*")

Frame(f1,bg="black",width=250,height=2).place(x=50,y=190)

Button(f1,width=20,pady=7,text="Sign Up",bg='#4db4f0',fg='black',border=0,command=signin).place(x=60,y=230)
lbl2=Label(f1,text="I have an acount",bg="#fff",fg="black",font=("Microsoft Yahei UI Light ",10))
lbl2.place(x=70,y=280)
btn=Button(f1,width=6,text="Sign up",highlightbackground="white",highlightthickness=-1,border=0,bg="white",fg="#57a1f8",cursor="hand1",command=signup)
btn.place(x=160,y=280)




root.mainloop()