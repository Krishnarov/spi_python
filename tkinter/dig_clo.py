from tkinter import *
import time
import sys
root=Tk()
root.title("Digital clock")
root.geometry("+250+200")

def get_time():
	tim=time.strftime("%I:%M:%S %p")
	clo.config(text=tim)
	clo.after(200,get_time)
clo=Label(root,font=("Calibri",100),bg="black",fg="white")
clo.pack()

get_time()

root.mainloop()
