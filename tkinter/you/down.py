import tkinter as tk
from tkinter import*
from pytube import YouTube
from tkinter import messagebox,filedialog

class downl():
    def __init__(self,root):
        self.root=root
        self.root.title("video downloder")
        self.root.geometry("600x500")
        self.root.resizable(False,False)


        self.don=StringVar()
        self.don1=StringVar()
        self.nt=StringVar()
        def exit():
            root.destroy()
        def clear():
            self.don1.set("")
            self.don.set("")
            var.set("select type")
            n.delete(0, END)
        def bro():
    
            dd=filedialog.askdirectory(initialdir="your directory path",title="save video")
            self.nt.set(dd)

        def ok():
            a=n.get()
            sel=var.get()
            df=self.nt.get()
    
            if sel=="mp3" and a!="":
        
                try:
                    video = YouTube(a)
                    stream = video.streams.filter(only_audio=True).first()
                    stream.download(df,filename=f"{video.title}.mp3")
                    self.don.set("Downloding successes.")
                except KeyError:
                    self.don1.set("Downloding Error")
                    print("Unable to fetch video information. Please check the video URL or your network connection.")
            elif sel=="mp4" and a!="":
        
                try:
                    video = YouTube(a)
                    stream = video.streams.get_highest_resolution()
                    stream.download(df,filename=f"{video.title}.mp4")
                    self.don.set("Downloding successes.")
            
            
                except KeyError:
                    self.don1.set("Downloding Error")
                    print("Unable to fetch video information. Please check the video URL or your network connection.")
        
            else:
        
                self.don1.set("Downloding Error")

        self.title=Label(root,text="Video Downloder",font=("times now roman",40),fg="#fff",bg="#f542a1").place(x=0,y=0,relwidth=1)
        fram=Frame(self.root,bg="#fff",bd=6,relief=RIDGE)
        fram.place(x=50,y=100,width=500,height=380)

        self.title1=Label(fram,text="Details",font=("goudy old style",30),fg="#fff",bg="#f59042").place(x=0,y=0,relwidth=1)
        im=PhotoImage(file="icon.png")
        lal=Label(root,image=im,width=50,height=50,bg="#f542a1").place(x=10,y=0)
        self.lbl1=Label(fram,text="Enter or Paste url on youtube video",font=("times now roman",20,"bold"),bg="#fff",fg="black").place(x=80,y=50)
        n=Entry(fram,font=("times now roman",15),bg="lightyellow",fg="black")
        n.place(x=50,y=90,width=380,height=35)
        self.lbl7=Label(fram,text="Select Destination",font=("times now roman",20,"bold"),bg="#fff",fg="black").place(x=160,y=135)
        n1=Entry(fram,textvariable=self.nt,font=("times now roman",15),bg="lightyellow",fg="black")
        n1.place(x=50,y=180,width=300,height=35)
        self.lbl2=Label(fram,text="Select Type",font=("times now roman",20,"bold"),bg="#fff",fg="black").place(x=110,y=220)

        self.typ=("mp3","mp4")
        var=StringVar(fram)
        var.set("select type")
        drp=OptionMenu(fram,var, "mp3", "mp4")
        drp.place(x=260,y=223,width=100)
        btn_b=Button(fram,text="Browse",font=("times now roman",18,"bold"),fg="black",bg="green",command=bro).place(x=350,y=180,width=80,height=35)
        btn_c=Button(fram,text="Clear",font=("times now roman",18,"bold"),fg="black",bg="green",command=clear).place(x=350,y=265,width=80,height=35)
        btn=Button(fram,text="Downlode",font=("times now roman",18,"bold"),fg="black",bg="green",command=ok).place(x=150,y=265,width=180,height=35)
        btn_x=Button(fram,text="Exit",font=("times now roman",18,"bold"),fg="black",bg="green",command=exit).place(x=50,y=265,width=80,height=35)
        self.lbl3=Label(fram,textvariable=self.don,font=("times now roman",20,"bold"),bg="#fff",fg="green").place(x=130,y=310)
        self.lbl4=Label(fram,textvariable=self.don1,font=("times now roman",20,"bold"),bg="#fff",fg="red").place(x=130,y=310)
        self.lbl5=Label(fram,text="Developed by:- ",font=("times now roman",10),bg="#fff",fg="black").place(x=300,y=340)
        self.lbl6=Label(fram,text="Er. Krishna Kumar",font=("times now roman",10,"bold"),bg="#fff",fg="black").place(x=380,y=340)


if __name__=="__main__":
    root=tk.Tk()
    app=downl(root)
    root.mainloop()
