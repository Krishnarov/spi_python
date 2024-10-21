from tkinter import *
import googletrans
from googletrans import Translator
#def translate():
	

root=Tk()
root.title("translate")
root.geometry("550x550+0+100")
root.config(bg="#fff")

lbl1=Label(root,text="Translate",bg="#fff",fg="blue",font=("Microsoft Yahei UI Light ",23," bold"))
lbl1.place(x=200,y=50)




lbl2=Label(root,text="text",bg="#fff",fg="blue",font=("Microsoft Yahei UI Light ",18," bold"))
lbl2.place(x=50,y=100)




t1=Text(root,font=("arial 20 bold"),bg="gray")
t1.place(x=50,y=130,width=320,height=100)

b1 = Button(root,text="Translate",fg="green", bg="gray",font=("Arial 20 bold"))
b1.place(x=380,y=100)
language=googletrans.LANGUAGES
langv=list(language.values())
menu=StringVar()
menu.set("select")
drop=OptionMenu(root,menu,*langv)
drop.place(x=300,y=100,width=150)



root.mainloop()