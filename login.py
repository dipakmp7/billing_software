from tkinter import *
from tkinter import messagebox

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("500x500")
        bg_color="brown"
        

        Label(self.root, text="USERNAME",bd=8,relief=GROOVE,width=13,bg=bg_color,font=("times new roman",15,"bold"),fg="white").place(x=50, y=170)
        Label(self.root, text="PASSWORD",bd=8,relief=GROOVE,width=13,bg=bg_color,font=("times new roman",15,"bold"),fg="white").place(x=50, y=220)

        e1=Entry(self.root)
        e1.place(height=30,width=200,x=250, y=170)

        e2=Entry(self.root)
        e2.place(height=30, width=200,x=250, y=220)
        e2.config(show="*")

       


        def login():
            uname=e1.get()
            passwd=e2.get()

            if(uname=="" and passwd==""):
                messagebox.showerror("Error","Please Enter ID and Password")

            elif(uname=="admin" and passwd=="1234"):
                messagebox.showinfo("Success","Login Successfull")
                self.root.destroy()
                import bill
                

            else:
                messagebox.showerror("Error","Incorrect Username and Password")
        
        Button(root, text="LOGIN", bd=6,command=login, fg="white",font=("times new roman",15,"bold"),height=2, width=15, relief=GROOVE,bg=bg_color).place(x=200, y=300)

root=Tk()
obj=login(root)
root.mainloop()

        
