from tkinter import*

root=Tk()
root.geometry("480x500")
root.title("images")
bg=PhotoImage(file="logo.png")
lbl=Label(root,image=bg)
lbl.place(x=0,y=0)
lbl1=Label(root,text="Dictionary",font=("Arial 30 bold"))
lbl1.place(x=100,y=40)


root.mainloop()