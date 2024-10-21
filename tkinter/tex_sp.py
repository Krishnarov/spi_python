#text to speech convereter
from gtts import gTTS
from tkinter import *
import os
root = Tk()
root.geometry("520x550+350+70")
frame1 = Frame(root,bg = "skyblue",height = "130")
frame1.pack(side = BOTTOM)
frame1.place(x=0,y=0,width=600,height=300)

frame2 = Frame(root,bg = "lightblue",height = "1000")
frame2.pack(side = BOTTOM)
frame2.place(x=0,y=130,width=600,height=700)

label = Label(frame1, text = "Text to Speech",font = "Arial 30 bold",fg = "red", bg="skyblue")
label.place(x = 60, y = 40,height=50,width=400)
entry =Text(frame2,bd = 4, font = 14, height=5,width=35,bg="white")
entry.place(x = 90, y = 30)
def play():
 language = "en"
 myobj = gTTS(text = entry.get("1.0",'end-1c'),lang =language,slow = False)
 myobj.save("convert.wav")
 os.system("start convert.wav")
btn = Button(root, text = "Speak",width = "16", pady = 10,font = "bold, 15",command = play, bg='red',fg="black")
btn.place(x=170,y=350)
root.title("text_to_speech_convertor")
root.mainloop()