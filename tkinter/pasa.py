from tkinter import*
import random

win=Tk()
win.title("game")
win.geometry("500x500+0+100")
#win.resize(False,False)
lab=Label(win,text="",font=("times",260))
def roll():
	dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	lab.configure(text=f'{random.choice(dice)}')
	lab.pack()

btn=Button(win,text="Let's roll...",width=40,height=5,font=10,bg="white",bd=2,command=roll)
btn.pack(padx=10,pady=10)




win.mainloop()