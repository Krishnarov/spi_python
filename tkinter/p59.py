import tkinter as tk
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to speech")
root.geometry("900x450+250+200")
root.resizable(False,False)
root.configure(bg="#305065")

eng=pyttsx3.init()

def speaknow():
	text=t_area.get(1.0,END)
	gender=g_com.get()
	speed=s_com.get()
	voice=eng.getProperty("Voice")

	def setvoice():
		if (gender=="Male"):
			eng.setProperty("voice",voice[0].id)
			eng.say(text)
			eng.runAndWait()
		else:
			eng.setProperty("voice",voice[1].id)
			eng.say(text)
			eng.runAndWait()
	if (text):
		if (speed=="Fast"):
			eng.setProperty("rate",250)
			setvoice()
		elif(speed=="Normal"):
			eng.setProperty("rate",150)
			setvoice()
		else:
			eng.setProperty("rate",60)
			setvoice()


t_frame=Frame(root,bg="white",width=900,height=100)
t_frame.place(x=0,y=0)

logo=PhotoImage(file="s logo.png")
Label(t_frame,image=logo,bg="white",width=90,height=95).place(x=10,y=5)

Label(t_frame,text="Text to speech",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

Label(root,text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="speed",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

t_area=Text(root,font="Robote 20 ",fg="black",bg="white",wrap=WORD)
t_area.place(x=10,y=150,width=500,height=250)

g_com=Combobox(root,values=["Male","Female"],font="arial 14",state="r",width=10)
g_com.place(x=550,y=200)
g_com.set("Male")

s_com=Combobox(root,values=["Fast","Normal","Slow"],font="arial 14",state="r",width=10)
s_com.place(x=730,y=200)
s_com.set("Normal")

btn=Button(root,text="Speak",width=10,font="arial 14 bold",command=speaknow())
btn.place(x=550,y=280)



save=Button(root,text="save",width=10,font="arial 14 bold")
save.place(x=730,y=280)



root.mainloop()