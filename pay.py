from abcd import callback
from tkinter import *
import math,random,os,datetime
from tkinter import messagebox 
from PIL import Image, ImageTk






class Pay_App:
	

	def __init__(self,root):
		self.root=root
		self.root.geometry("1350x750+0+0")
		self.root.title("Payment")
		
        
		title=Label(self.root,text="Payment",bd=12,relief=GROOVE,bg="brown",fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
		link1 = Label(root, text="Pay With Link", cursor="hand2",bg="brown",fg="white",bd=2,pady=8,width=10,font="arial 15 bold")
		link1.place(x=850, y=250, height=100, width=200)
		link1.bind("<Button-1>", lambda e: callback("https://dashboard.paytm.com/next/payment-link"))

		btn_back = Button(self.root, text="BACK", font=("times new roman", 15, "bold"), cursor="hand2", bd=1,
                          fg="white",
                          bg="brown", command=self.back_window).place(x=850, y=400, width=200, height=100)

		
		
		
		self.left1 = ImageTk.PhotoImage(Image.open("download.jpeg"))
		left1 = Label(self.root, image=self.left1).place(x=100, y=150, height=500, width=450)

	

	def back_window(self):
		self.root.destroy()
		import bill
		root.mainloop()
	
root=Tk()
obj=Pay_App(root)
root.mainloop()