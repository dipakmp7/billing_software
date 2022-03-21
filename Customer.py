import tkinter
from tkinter import *
import mysql.connector as sql
from tkinter import messagebox, ttk
import random


class CustomerChart_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Chart")
        self.root.geometry("1350x700+0+0")
        self.root.maxsize(1350, 700)
        self.root.config(bg="orange")

        # Bg...Image
        #self.bg1 = ImageTk.PhotoImage(file="/Images/RegisterBg.jpg")
        #bg1 = Label(self.root, image=self.bg1, bg="black").place(x=700, y=0, relwidth=1, relheight=1)

        #self.bg2 = ImageTk.PhotoImage(file="/Images/Blur.jpg")
        #bg2 = Label(self.root, image=self.bg2, bg="white").place(x=0, y=0, width=640, relheight=1)
        left_lbl=Label(self.root, bg="orange",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=350)

        right_lbl = Label(self.root, bg="black", bd=0)
        right_lbl.place(x=450, y=0, relheight=1, relwidth=1)

        # LoginFrame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=175, y=50, width=1000, height=600)


        title = Label(frame1, text="CUSTOMER CHART", font=("times new roman", 20, "bold"), bg="white",fg="lightgray").place(x=370, y=20)

        search = Label(frame1, text="Search By:", font=("times new roman", 15), bg="white", fg="black").place(x=100,y=70)
        self.cmb_search = ttk.Combobox(frame1, font=("times new roman", 10), state='readonly', justify=CENTER)
        self.cmb_search['values'] = ("Select", "Bill Number", "Customer Name")
        self.cmb_search.place(x=200, y=72, width="170", height='25')
        self.cmb_search.current(0)

        self.txt_searchbar = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_searchbar.place(x=400, y=72, width="170", height='25')

        btn_search = Button(frame1, text="Search", font=("times new roman", 15), cursor="hand2", bd=1,
                            fg="white",
                            bg="#4181c4", command=self.search_data).place(x=600, y=70, width=100, height=27)

        btn_clear = Button(frame1, text="Clear", font=("times new roman", 15), cursor="hand2", bd=1,
                           fg="white",
                           bg="#4181c4", command=self.clear).place(x=730, y=70, width=100, height=27)

        btn_back = Button(frame1, text="BACK", font=("times new roman", 15, "bold"), cursor="hand2", bd=1,
                          fg="black",
                          bg="lightgray", command=self.back_window).place(x=310, y=450, width=100, height=35)

        btn_delete = Button(frame1, text="DELETE", font=("times new roman", 15, "bold"), cursor="hand2", bd=1,
                            fg="black",
                            bg="red", command=self.delete_data).place(x=510, y=450, width=100, height=35)





        frame2 = Frame(self.root, bg="white")
        frame2.place(x=250, y=170, width=820, height=300)

        scroll_x = Scrollbar(frame2, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame2, orient=VERTICAL)
        self.search_table = ttk.Treeview(frame2, height=300, columns=("bill_number", "c_name", "c_phone_number", "total"),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.search_table.xview)
        scroll_y.config(command=self.search_table.yview)
        self.search_table.heading("bill_number", text="Bill Number")
        self.search_table.heading("c_name", text="Customer Name")
        self.search_table.heading("c_phone_number", text="Contact")
        self.search_table.heading("total", text="Total Amount")
        self.search_table["show"] = 'headings'
        self.search_table.column("bill_number", width=100)
        self.search_table.column("c_name", width=200)
        self.search_table.column("c_phone_number", width=300)
        self.search_table.column("total", width=100)
        self.search_table.pack()
        self.fetch_data()

    def clear(self):
        self.txt_searchbar.delete(0, END)
        self.cmb_search.set("Select")

    def fetch_data(self):
        try:
            conn = sql.connect(
                host="localhost",
                database="bill",
                user="root",
                password='12345')
            cur = conn.cursor()
            cur.execute("select bill_number, c_name, c_phone_number, total from bill_table")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.search_table.delete(*self.search_table.get_children())
            for row in rows:
                self.search_table.insert('', END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def search_data(self):
        if self.cmb_search.get() == "Select":
            conn = sql.connect(
                host="localhost",
                database="bill",
                user="root",
                password='12345')
            cur = conn.cursor()
            cur.execute("select bill_number, c_name, c_phone_number, total from bill_table")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.search_table.delete(*self.search_table.get_children())
                for row in rows:
                    self.search_table.insert('', END, values=row)
                    conn.commit()
                    self.txt_searchbar.delete(0, END)
            conn.close()
        elif self.cmb_search.get() == "Bill Number":
            conn = sql.connect(
                host="localhost",
                database="bill",
                user="root",
                password='12345')
            cur = conn.cursor()
            cur.execute("select * from bill_table where bill_number LIKE " + self.txt_searchbar.get())
            rows = cur.fetchall()
            if len(rows) != 0:
                self.search_table.delete(*self.search_table.get_children())
                for row in rows:
                    self.search_table.insert('', END, values=row)
                    conn.commit()
            conn.close()
        else:
            conn = sql.connect(
                host="localhost",
                database="bill",
                user="root",
                password='12345')
            cur = conn.cursor()
            cur.execute("select * from bill_table where c_name LIKE '%" + self.txt_searchbar.get() + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.search_table.delete(*self.search_table.get_children())
                for row in rows:
                    self.search_table.insert('', END, values=row)
                    conn.commit()
            conn.close()

    def delete_data(self):
        cur_row = self.search_table.focus()
        content = self.search_table.item(cur_row)
        row = content['values']
        bill1 =row[0]
        conn = sql.connect(
            host="localhost",
            database="bill",
            user="root",
            password='12345')
        cur = conn.cursor()
        cur.execute("delete from bill_table where bill_number LIKE " + str(bill1))
        conn.commit()
        conn.close()
        self.fetch_data()
        


   

    def back_window(self):
        self.root.destroy()
        import bill
        root.mainloop()
        
        


root = Tk()
obj = CustomerChart_window(root)
root.mainloop()
