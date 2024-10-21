from tkinter import*
from tkinter import messagebox
import ast
root=Tk()
root.title("Login")
root.geometry("500x800")
root.config(bg="#fff")
root.resizable(False,False)

f1=Frame(root,bg='gray',height=600,width=300)
f1.place(x=100,y=100)

#img=PhotoImage(file="pn2.png")
#lbl=Label(f1,image=img,border=0,bg="#fff")
#lbl.place(x=50,y=50,height=250,width=200)
f2=Frame(f1,bg='#fff',height=250,width=200)
f2.place(x=50,y=50)

f3=Frame(f1,bg='#fff',height=150,width=180)
f3.place(x=40,y=320)
bt1=Button(f3,bg="gray",pady=5,border=0,text="1",font=("arial",10,"bold"),fg="black")
bt1.place(x=5,y=5)
bt2=Button(f3,bg="gray",pady=5,border=0,text="2",font=("arial",10,"bold"),fg="black")
bt2.place(x=45,y=5)
bt3=Button(f3,bg="gray",pady=5,border=0,text="3",font=("arial",10,"bold"),fg="black")
bt3.place(x=85,y=5)
bt4=Button(f3,bg="gray",pady=8,border=0,text="←",font=("arial",10,"bold"),fg="black")
bt4.place(x=130,y=5)

bt5=Button(f3,bg="gray",pady=5,border=0,text="4",font=("arial",10,"bold"),fg="black")
bt5.place(x=5,y=40)
bt6=Button(f3,bg="gray",pady=5,border=0,text="5",font=("arial",10,"bold"),fg="black")
bt6.place(x=45,y=40)
bt7=Button(f3,bg="gray",pady=5,border=0,text="6",font=("arial",10,"bold"),fg="black")
bt7.place(x=85,y=40)
bt8=Button(f3,bg="gray",pady=8,border=0,text="↳",font=("arial",10,"bold"),fg="black")
bt8.place(x=130,y=40)

bt9=Button(f3,bg="gray",pady=5,border=0,text="7",font=("arial",10,"bold"),fg="black")
bt9.place(x=5,y=80)
bt10=Button(f3,bg="gray",pady=5,border=0,text="8",font=("arial",10,"bold"),fg="black")
bt10.place(x=45,y=80)
bt11=Button(f3,bg="gray",pady=5,border=0,text="9",font=("arial",10,"bold"),fg="black")
bt11.place(x=85,y=80)
bt12=Button(f3,bg="gray",pady=5,border=0,text="0",font=("arial",10,"bold"),fg="black")
bt12.place(x=130,y=80)




root.mainloop()
