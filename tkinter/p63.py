from tkinter import*

root=Tk()
root.geometry("500x700")
root.title("From")
root.config(bg="azure3")
f1=Frame(root,highlightbackground="blue", highlightthickness=2,height=600,width=400)
f1.place(x=50,y=50)
lbl1=Label(f1,taxt="Enter your name : ",font=("arial 15 bold"),bg="white")

n1 = Entry(f1,width=35,fg='black',highlightbackground="white",highlightthickness=0,border=2,bg='white',font=('Microsoft Yahei UI Light',11))
n1.place(x=50,y=100)
n1.insert(0,'Username')
n1.bind('<FocusIn>',on_enter)
n1.bind('<FocusOut>',on_leave)
#n1.pack()

Frame(f1,bg="black",width=250,height=2).place(x=50,y=120)



root.mainloop()
