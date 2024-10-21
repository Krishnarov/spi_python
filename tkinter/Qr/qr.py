from tkinter import*
import qrcode
from PIL import Image,ImageTk
import ast
from resizeimage import resizeimage
class Qr:
	def __init__(self,root):
		self.root=root
		self.root.geometry("900x500")
		self.root.title("Qr generator")
		self.root.resizable(False,False)

		title=Label(self.root,text="Qr Code Generator",font=("times now roman",40),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)

		self.var_en=StringVar()
		self.var_name=StringVar()
		self.var_sub=StringVar()
		self.var_coll=StringVar()

		fram=Frame(self.root,bg="#fff",bd=6,relief=RIDGE)
		fram.place(x=50,y=100,width=500,height=380)
		title1=Label(fram,text="Student Details",font=("goudy old style",20),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)

		lbl1=Label(fram,text="Enrollment No.",font=("times now roman",15,"bold"),bg="#fff").place(x=20,y=50)
		lbl2=Label(fram,text="Student Name",font=("times now roman",15,"bold"),bg="#fff").place(x=20,y=100)
		lbl3=Label(fram,text="Subject",font=("times now roman",15,"bold"),bg="#fff").place(x=20,y=150)
		lbl4=Label(fram,text="Collage Name",font=("times now roman",15,"bold"),bg="#fff").place(x=20,y=200)

		n1=Entry(fram,font=("times now roman",15,"bold"),textvariable=self.var_en,bg="lightyellow").place(x=200,y=50)
		n2=Entry(fram,font=("times now roman",15,"bold"),textvariable=self.var_name,bg="lightyellow").place(x=200,y=100)
		n3=Entry(fram,font=("times now roman",15,"bold"),textvariable=self.var_sub,bg="lightyellow").place(x=200,y=150)
		n4=Entry(fram,font=("times now roman",15,"bold"),textvariable=self.var_coll,bg="lightyellow").place(x=200,y=200)




		btn=Button(fram,text="Qr Code Generator",font=("times now roman",18,"bold"),fg="black",bg="green",command=self.generat).place(x=90,y=250,width=180,height=30)
		btn1=Button(fram,text="Clear",font=("times now roman",18,"bold"),fg="black",bg="green",command=self.clear).place(x=300,y=250,width=100,height=30)

		self.msg=""
		self.lbl5=Label(fram,text=self.msg,font=("times now roman",20),fg="green",bg="#fff")
		self.lbl5.place(x=100,y=300)

		fram1=Frame(self.root,bg="#fff",bd=6,relief=RIDGE)
		fram1.place(x=600,y=100,width=250,height=380)
		title2=Label(fram1,text="QR Code",font=("goudy old style",20),fg="#fff",bg="green").place(x=0,y=0,relwidth=1)
		self.lbl6=Label(fram1,text="QR not ablavel",font=("times now roman",15),fg="#fff",bg="green",bd=2,relief=RIDGE)
		self.lbl6.place(x=35,y=100,width=180,height=180)

	def generat(self):
		if self.var_en.get()=="" or self.var_name.get()=="" or self.var_sub.get()=="" or self.var_coll.get()=="":
			self.msg="All filde are required"
			self.lbl5.config(text=self.msg,fg="red")
		else:

			data=(f"Enrollment No: {self.var_en.get()}\n\nStudent Name : {self.var_name.get()}\n\nSubject : {self.var_sub.get()}\n\ncollage Name : {self.var_coll.get()}")
			qr_code=qrcode.make(data)
			qr_code=resizeimage.resize_cover(qr_code,[180,180])
			qr_code.save("code/stu_"+str(self.var_name.get())+'.png')
			self.im=ImageTk.PhotoImage(file="code/stu_"+str(self.var_name.get())+'.png')
			self.lbl6.config(image=self.im)
			self.msg="QR Generator Successfuly"
			self.lbl5.config(text=self.msg,fg="green")
			try:
				file=open("datasheet.txt","r+")
				k=file.read()
				l=ast.literal_eval(k)
				p={(f"Enrollment No: {self.var_en.get()}\n\nStudent Name : {self.var_name.get()}\n\nSubject : {self.var_sub.get()}\n\ncollage Name : {self.var_coll.get()}")}
				l.update(str(p))
				file.truncate(0)
				file.close()
				file=open("datasheet.txt","w")
				w=file.write(str(l))
			except:
				file=open("datasheet.txt","r+")
				k=file.read()
				l=ast.literal_eval(k)
				p={f"Enrollment No: {self.var_en.get()}\n\nStudent Name : {self.var_name.get()}\n\nSubject : {self.var_sub.get()}\n\ncollage Name : {self.var_coll.get()}"}
				l.update(p)
				file.truncate(0)
				file.close()
				file=open("datasheet.txt","w")
				w=file.write(str(l))




			
			
			
			
			
			

			

	def clear(self):
		self.var_en.set('')
		self.var_name.set('')
		self.var_sub.set('')
		self.var_coll.set('')
		self.msg=''
		self.lbl5.config(text=self.msg)
		self.lbl6.config(image='')





root=Tk()
obj=Qr(root)

root.mainloop()
