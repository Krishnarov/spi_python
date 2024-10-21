from tkinter import *
import ast
from tkinter import messagebox
def find():
 i=entry.get()
 file=open('datasheet.txt','r+')
 d=file.read()
 r=ast.literal_eval(d)
 file.close()
 if i in r.keys():
  lbl2.config(text=(r[i]),fg="black")
  
 else:
  lbl2.config(text="Not Found",fg="black")
#--------------------------------------------
def add():
    win=Toplevel(root)
    win.title("Oxford dictionary")
    win.geometry("500x500")
    win.config(background="gray")


    def add_d():
        word=entry.get()

        mins=entry1.get()
        dict2={word:mins}
        if word=="" or mins=="":
            messagebox.showwarning("Invalid","plesse enter value")
        
        else:
            file=open("datasheet.txt",'r+')
            d=file.read()
            r=ast.literal_eval(d)
            r.update(dict2)
            file.truncate(0)
            file.close()
    
            file=open("datasheet.txt","w")
            file.write(str(r))
            file.close()
            messagebox.showinfo("","add this word meaning in dictionary")
        entry.delete(0,'end')
        entry1.delete(0,'end')



    frame=Frame(win)
    frame.pack()
    bframe=Frame(win)
    bframe.pack(side = BOTTOM)
    bframe.place(width=500,height=700)
    bframe.config(bg="gold")
    lbl1=Label(bframe,text="Oxford dictionary",fg="black",font=("calibri 25 bold"),bg="gold")
    lbl1.place(x=140,y=40)
    lbl2=Label(bframe,text="Enter word",fg="black",font=("calibri 15 bold"),bg="gold")
    lbl2.place(x=120,y=100)
    entry=Entry(bframe,fg="black",font=("calibri 20 "),bg="white")
    entry.place(x=120,y=125)

    lbl3=Label(bframe,text="Enter Maning",fg="black",font=("calibri 15 bold"),bg="gold")
    lbl3.place(x=120,y=220)
    entry1=Entry(bframe,fg="black",font=("calibri 20 "),bg="white")
    entry1.place(x=120,y=250)

    button1 = Button(bframe, text="Add", fg="black", bg="black",font=("Arial 20 bold"),command=add_d)
    button1.place(x=200,y=400)

    win.mainloop()


#-------------------------------------------------------
root=Tk()
def clear():
    entry.delete(0,'end')
    lbl2.config(text="")


root.title("Oxford dictionary")
root.geometry("500x500")
root.config(background="gray")
frame=Frame(root)
frame.pack()
bframe=Frame(root)
bframe.pack(side = BOTTOM)
bframe.place(width=500,height=700)
bframe.config(bg="gold")
lbl1=Label(bframe,text="Oxford dictionary",fg="black",font=("calibri 25 bold"),bg="gold")
lbl1.place(x=140,y=40)

def on_enter(e):
    entry.delete(0,'end')
def on_leave(e):
    if entry.get()=="":
        entry.insert(0,"Enter word")
entry=Entry(bframe,fg="black",font=("calibri 20 "),bg="white")
entry.place(x=120,y=120)
entry.insert(0,'Enter word')
entry.bind('<FocusIn>',on_enter)
entry.bind('<FocusOut>',on_leave)
lbl2=Label(bframe,font=("Calibri 35 bold"),bg="gold",fg="black")
lbl2.place(height=110,width=240,x=130,y=200)


button = Button(bframe, pady=8,text="Search", fg="black", bg="black",font=("Arial 20 bold") ,command=find)
button.place(x=45,y=350,width=200)
button2 = Button(bframe, pady=8,text="Clear", fg="black", bg="black",font=("Arial 20 bold") ,command=clear)
button2.place(x=265,y=350,width=200)
button1 = Button(bframe, pady=8,text="Add word", fg="black", bg="black",font=("Arial 20 bold") ,command=add)
button1.place(x=160,y=420,width=200)


root.mainloop()
