from email.message import EmailMessage
from tkinter import *
import math
import random
import os
import datetime
from tkinter import messagebox, ttk
import mysql.connector as sql
import smtplib
from reportlab.pdfgen import canvas
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Billing Software")
        bg_color = "brown"
        title = Label(self.root, text="SAI DAIRY", bd=12, relief=GROOVE, bg=bg_color,
                      fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        exit_btn = Button(self.root, text="Customer Details", command=self.customer, bg=bg_color,
                          fg="white", bd=2, pady=8, width=10, font="arial 15 bold").pack(side=BOTTOM, fill=X)

        # variables

        # Products

        self.cow_milk_txt = IntVar()
        self.buffalo_milk_txt = IntVar()
        self.butter_milk_txt = IntVar()
        self.curd_txt = IntVar()
        self.paneer_txt = IntVar()

        self.cow = IntVar()
        self.buffalo = IntVar()
        self.butter_milk = IntVar()
        self.curd = IntVar()
        self.paneer = IntVar()
        self.flav_milk = IntVar()

        # Products2

        self.shrikhand_txt = IntVar()
        self.amrakhand_txt = IntVar()
        self.cow_ghee_txt = IntVar()
        self.buffalo_ghee_txt = IntVar()

        self.shrikhand = IntVar()
        self.amrakhand = IntVar()
        self.cow_ghee = IntVar()
        self.buffalo_ghee = IntVar()
        self.butter = IntVar()
        self.lassi = IntVar()

        # Cold Drink

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # Total Product Price and Tax Variables

        self.product_price = StringVar()
        self.product2_price = StringVar()
        self.cold_drink_price = StringVar()

        self.product_tax = StringVar()
        self.product2_tax = StringVar()
        self.cold_drink_tax = StringVar()
        self.email = StringVar()

        # Customer

        self.c_name = StringVar()
        self.c_phn = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # Customer Detail Frame

        F1 = LabelFrame(self.root, text="Customer Details", bd=12, relief=GROOVE,
                        bg=bg_color, font=("times new roman", 15, "bold"), fg="gold")
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=(
            "times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15",
                          bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        cphn_lbl = Label(F1, text="Customer Phone No", bg=bg_color, fg="white", font=(
            "times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phn, font="arial 15",
                         bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        # Product1 Frame

        F2 = LabelFrame(self.root, text="Dairy Product", bd=10, relief=GROOVE,
                        bg=bg_color, font=("times new roman", 15, "bold"), fg="gold")
        F2.place(x=5, y=180, width=325, height=380)

        cow_milk_lbl = Label(F2, text="Cow Milk",  font=("times new roman", 16, "bold"),
                             bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cow_milk_txt = Entry(F2, width=10, textvariable=self.cow_milk_txt,  font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        cow_milk_txt.place(x=170, y=10, width=60, height=30)

        self.cow = ttk.Combobox(F2, width=10, font=(
            "times new roman", 12, "bold"))
        self.cow['values'] = ("0", "1 Lit", "500 ml", "250 ml")
        self.cow.place(x=240, y=10, width=60, height=30)
        self.cow.current(0)

        buff_milk_lbl = Label(F2, text="Buffalo Milk", font=("times new roman", 16, "bold"),
                              bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        buff_milk_txt = Entry(F2, width=10, textvariable=self.buffalo_milk_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        buff_milk_txt.place(x=170, y=60, width=60, height=30)
        self.buffalo = ttk.Combobox(
            F2, width=10, font=("times new roman", 12, "bold"))
        self.buffalo['values'] = ("0", "1 Lit", "500 ml", "250 ml")
        self.buffalo.place(x=240, y=60, width=60, height=30)
        self.buffalo.current(0)

        butter_milk_lbl = Label(F2, text="Butter Milk", font=("times new roman", 16, "bold"),
                                bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        butter_milk_txt = Entry(F2, width=10, textvariable=self.butter_milk_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        butter_milk_txt.place(x=170, y=110, width=60, height=30)
        self.butter_milk = ttk.Combobox(
            F2, width=10, font=("times new roman", 12, "bold"))
        self.butter_milk['values'] = ("0", "1 Lit", "500 ml", "250 ml")
        self.butter_milk.place(x=240, y=110, width=60, height=30)
        self.butter_milk.current(0)

        curd_lbl = Label(F2, text="Curd", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        curd_txt = Entry(F2, width=10, textvariable=self.curd_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        curd_txt.place(x=170, y=160, width=60, height=30)
        self.curd = ttk.Combobox(
            F2, width=10, font=("times new roman", 12, "bold"))
        self.curd['values'] = ("0", "1 kg", "500 gm", "250 gm")
        self.curd.place(x=240, y=160, width=60, height=30)
        self.curd.current(0)

        paneer_lbl = Label(F2, text="Paneer", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        paneer_txt = Entry(F2, width=10, textvariable=self.paneer_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        paneer_txt.place(x=170, y=210, width=60, height=30)
        self.paneer = ttk.Combobox(
            F2, width=10, font=("times new roman", 12, "bold"))
        self.paneer['values'] = ("0", "1 kg", "500 gm", "250 gm")
        self.paneer.place(x=240, y=210, width=60, height=30)
        self.paneer.current(0)

        flav_milk_lbl = Label(F2, text="Flavoured Milk", font=("times new roman", 16, "bold"),
                              bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        flav_milk_txt = Entry(F2, width=10, textvariable=self.flav_milk, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Product2 Frame

        F3 = LabelFrame(self.root, text="Dairy Product", bd=10, relief=GROOVE,
                        bg=bg_color, font=("times new roman", 15, "bold"), fg="gold")
        F3.place(x=340, y=180, width=325, height=380)

        shrikhand_lbl = Label(F3, text="Shrikhand", font=("times new roman", 16, "bold"),
                              bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        shrikhand_txt = Entry(F3, width=10, textvariable=self.shrikhand_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        shrikhand_txt.place(x=160, y=10, width=60, height=30)
        self.shrikhand = ttk.Combobox(
            F3, width=10, font=("times new roman", 12, "bold"))
        self.shrikhand['values'] = ("0", "1 kg", "500 gm", "250 gm")
        self.shrikhand.place(x=230, y=10, width=60, height=30)
        self.shrikhand.current(0)

        amrakhand_lbl = Label(F3, text="Amrakhand", font=("times new roman", 16, "bold"),
                              bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        amrakhand_txt = Entry(F3, width=10, textvariable=self.amrakhand_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        amrakhand_txt.place(x=160, y=60, width=60, height=30)
        self.amrakhand = ttk.Combobox(
            F3, width=10, font=("times new roman", 12, "bold"))
        self.amrakhand['values'] = ("0", "1 kg", "500 gm", "250 gm")
        self.amrakhand.place(x=230, y=60, width=60, height=30)
        self.amrakhand.current(0)

        cow_ghee_lbl = Label(F3, text="Cow Ghee", font=("times new roman", 16, "bold"),
                             bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        cow_ghee_txt = Entry(F3, width=10, textvariable=self.cow_ghee_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        cow_ghee_txt.place(x=160, y=110, width=60, height=30)
        self.cow_ghee = ttk.Combobox(
            F3, width=10, font=("times new roman", 12, "bold"))
        self.cow_ghee['values'] = ("0", "1 kg", "500 gm", "250 gm")
        self.cow_ghee.place(x=230, y=110, width=60, height=30)
        self.cow_ghee.current(0)

        buffalo_ghee_lbl = Label(F3, text="Buffalo Ghee", font=("times new roman", 16, "bold"),
                                 bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        buffalo_ghee_txt = Entry(F3, width=10, textvariable=self.buffalo_ghee_txt, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        buffalo_ghee_txt.place(x=160, y=160, width=60, height=30)
        self.buffalo_ghee = ttk.Combobox(
            F3, width=10, font=("times new roman", 12, "bold"))
        self.buffalo_ghee['values'] = ("0", "1 kg", "500 gm", "250 gm")
        self.buffalo_ghee.place(x=230, y=160, width=60, height=30)
        self.buffalo_ghee.current(0)

        butter_lbl = Label(F3, text="Butter", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        butter_txt = Entry(F3, width=10, textvariable=self.butter, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        lassi_lbl = Label(F3, text="Lassi", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        lassi_txt = Entry(F3, width=10, textvariable=self.lassi, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Coldrink Frame

        F4 = LabelFrame(self.root, text="Coldrink", bd=10, relief=GROOVE,
                        bg=bg_color, font=("times new roman", 15, "bold"), fg="gold")
        F4.place(x=670, y=180, width=325, height=380)

        maza_lbl = Label(F4, text="Maaza", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        maza_txt = Entry(F4, width=10, textvariable=self.maza, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        cock_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cock_txt = Entry(F4, width=10, textvariable=self.cock, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        frooti_lbl = Label(F4, text="frooti", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        frooti_txt = Entry(F4, width=10, textvariable=self.frooti, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        thumsup_lbl = Label(F4, text="Thums Up", font=("times new roman", 16, "bold"),
                            bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        thumsup_txt = Entry(F4, width=10, textvariable=self.thumsup, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        limca_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_txt = Entry(F4, width=10, textvariable=self.limca, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        sprite_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=(
            "times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Bill Area

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)
        bill_title = Label(F5, text="Bill Counter",
                           font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame

        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE,
                        bg=bg_color, font=("times new roman", 15, "bold"), fg="gold")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Product Price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.product_price, bd=7, font=(
            "arial", 10, "bold"), relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F1, text="Email", bg=bg_color, fg="white", font=(
            "times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=10, sticky="w")
        m2_txt = Entry(F1, width=30, textvariable=self.email, bd=7, font=(
            "arial", 12,), relief=SUNKEN).grid(row=0, column=5, padx=10, pady=1)

        c1_lbl = Label(F6, text="CGST", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.product_tax, bd=7, font=(
            "arial", 10, "bold"), relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c_bill_lbl = Label(F6, text="Bill No", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        c_bill_txt = Entry(F6, width=18, textvariable=self.search_bill, font=(
            "arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        bill_btn = Button(F6, text="Search", command=self.find_bill, width=15, bd=5, font=(
            "arial", 10, "bold")).grid(row=2, column=2, padx=10, pady=1)

        #c2_lbl=Label(F6,text="Product Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        # c2_txt=Entry(F6,width=18,textvariable=self.product2_tax,bd=7,font=("arial",10,"bold"),relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(F6, text="SGST", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, bd=7, font=(
            "arial", 10, "bold"), relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=700, width=630, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg=bg_color, fg="white",
                           bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        gbill_btn = Button(btn_F, command=self.bill_area, text="Generate Bill", bg=bg_color, fg="white",
                           bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg=bg_color, fg="white",
                           bd=2, pady=15, width=8, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        pay_btn = Button(btn_F, text="Pay", command=self.pay, bg=bg_color, fg="white", bd=2,
                         pady=15, width=8, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)

        exit_btn = Button(btn_F, text="Exit", command=self.exit_app, bg=bg_color, fg="white",
                          bd=2, pady=15, width=7, font="arial 15 bold").grid(row=0, column=4, padx=5, pady=5)
        self.welcome_bill()

    def total(self):

        if(self.cow.get() == "0"):
            self.c_s_p = 0*46
        elif(self.cow.get() == "1 Lit"):
            self.c_s_p = 1*46
        elif(self.cow.get() == "500 ml"):
            self.c_s_p = 0.5*46
        elif(self.cow.get() == "250 ml"):
            self.c_s_p = 0.25*46

        self.cow_price_final = self.c_s_p * int(self.cow_milk_txt.get())

        if(self.buffalo.get() == "0"):
            self.c_fc_p = 0*41
        elif(self.buffalo.get() == "1 Lit"):
            self.c_fc_p = 1*41
        elif(self.buffalo.get() == "500 ml"):
            self.c_fc_p = 0.5*41
        elif(self.buffalo.get() == "250 ml"):
            self.c_fc_p = 0.25*41

        self.buffalo_price_final = self.c_fc_p * \
            int(self.buffalo_milk_txt.get())

        if(self.butter_milk.get() == "0"):
            self.c_fw_p = 0*21
        elif(self.butter_milk.get() == "1 Lit"):
            self.c_fw_p = 1*21
        elif(self.butter_milk.get() == "500 ml"):
            self.c_fw_p = 0.5*21
        elif(self.butter_milk.get() == "250 ml"):
            self.c_fw_p = 0.25*21

        self.butter_price_final = self.c_fw_p * \
            int(self.butter_milk_txt.get())

        if(self.curd.get() == "0"):
            self.c_hs_p = 0*41
        elif(self.curd.get() == "1 kg"):
            self.c_hs_p = 1*41
        elif(self.curd.get() == "500 gm"):
            self.c_hs_p = 0.5*41
        elif(self.curd.get() == "250 gm"):
            self.c_hs_p = 0.25*41

        self.curd_final = self.c_hs_p * \
            int(self.curd_txt.get())

        if(self.paneer.get() == "0"):
            self.c_hg_p = 0*91
        elif(self.paneer.get() == "1 kg"):
            self.c_hg_p = 1*91
        elif(self.paneer.get() == "500 gm"):
            self.c_hg_p = 0.5*91
        elif(self.paneer.get() == "250 gm"):
            self.c_hg_p = 0.25*91

        self.paneer_final = self.c_hg_p * \
            int(self.paneer_txt.get())

        # self.c_s_p=int(self.cow.get())*46
        # self.c_fc_p=int(self.buffalo.get())*41
        # self.c_fw_p=self.butter_milk.get()*21
        # self.c_hs_p=self.curd.get()*41
        # self.c_hg_p=self.paneer.get()*91
        self.c_bl_p = self.flav_milk.get()*31

        if(self.shrikhand.get() == "0"):
            self.g_r_p = 0*81
        elif(self.shrikhand.get() == "1 kg"):
            self.g_r_p = 1*81
        elif(self.shrikhand.get() == "500 gm"):
            self.g_r_p = 0.5*81
        elif(self.shrikhand.get() == "250 gm"):
            self.g_r_p = 0.25*81

        self.shrikhand_final = self.g_r_p * \
            int(self.shrikhand_txt.get())

        if(self.amrakhand.get() == "0"):
            self.g_f_p = 0*95
        elif(self.amrakhand.get() == "1 kg"):
            self.g_f_p = 1*95
        elif(self.amrakhand.get() == "500 gm"):
            self.g_f_p = 0.5*95
        elif(self.amrakhand.get() == "250 gm"):
            self.g_f_p = 0.25*95

        self.amrakhand_final = self.g_f_p * \
            int(self.amrakhand_txt.get())

        if(self.cow_ghee.get() == "0"):
            self.g_d_p = 0*241
        elif(self.cow_ghee.get() == "1 kg"):
            self.g_d_p = 1*241
        elif(self.cow_ghee.get() == "500 gm"):
            self.g_d_p = 0.5*241
        elif(self.cow_ghee.get() == "250 gm"):
            self.g_d_p = 0.25*241

        self.cow_ghee_final = self.g_d_p * \
            int(self.cow_ghee_txt.get())

        if(self.buffalo_ghee.get() == "0"):
            self.g_w_p = 0*241
        elif(self.buffalo_ghee.get() == "1 kg"):
            self.g_w_p = 1*241
        elif(self.buffalo_ghee.get() == "500 gm"):
            self.g_w_p = 0.5*241
        elif(self.buffalo_ghee.get() == "250 gm"):
            self.g_w_p = 0.25*241

        self.buffalo_ghee_final = self.g_w_p * \
            int(self.buffalo_ghee_txt.get())

        # self.g_r_p=self.shrikhand.get()*81
        # self.g_f_p=self.amrakhand.get()*91
        # self.g_d_p=self.cow_ghee.get()*241
        # self.g_w_p=self.buffalo_ghee.get()*241
        self.g_s_p = self.butter.get()*41
        self.g_t_p = self.lassi.get()*21

        self.d_m_p = self.maza.get()*61
        self.d_c_p = self.cock.get()*61
        self.d_f_p = self.frooti.get()*41
        self.d_t_p = self.thumsup.get()*41
        self.d_l_p = self.limca.get()*41
        self.d_s_p = self.sprite.get()*61

        self.total_product_price = float(
            self.cow_price_final +
            self.buffalo_price_final +
            self.curd_final +
            self.butter_price_final +
            self.paneer_final +
            self.c_bl_p +

            self.shrikhand_final +
            self.amrakhand_final +
            self.cow_ghee_final +
            self.buffalo_ghee_final +
            self.g_s_p +
            self.g_t_p +


            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )
        self.product_price.set("Rs. "+str(self.total_product_price))
        self.p_tax = self.total_product_price*0.05
        self.d_tax = self.total_product_price*0.05
        self.product_tax.set("Rs. "+str("%.2f" % self.p_tax))
        self.cold_drink_tax.set("Rs. "+str("%.2f" % self.d_tax))

        self.Total_bill = int(self.total_product_price +
                              self.p_tax +
                              # self.p2_tax+
                              self.d_tax
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome!! Sai Dairy")
        self.txtarea.insert(END, f"\n Bill No : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone No : {self.c_phn.get()}")

        raw_TS = datetime.datetime.now()
        self.bbb = raw_TS.strftime("%d/%m/%Y")
        self.txtarea.insert(END, f"\n Date: {str(self.bbb)}")

        self.txtarea.insert(END, f"\n=====================================")
        self.txtarea.insert(END, f"\n Products\t\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n=====================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phn.get() == "" or self.email.get() == "":
            messagebox.showerror("Error", "Customer details are must....")
        elif self.check() == False:
            messagebox.showerror("Error", "Enter a valid email")
        elif self.product_price.get() == "Rs. 0.0" and self.product2_tax.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected....")
        elif (str(self.c_phn.get())).isnumeric() != True or len(str(self.c_phn.get())) != 10:
            messagebox.showerror("Error", "Phone number is not valid")
        else:
            self.welcome_bill()

            # Product

            if self.cow_milk_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.cow.get()} Cow Milk \t\t\t{self.cow_milk_txt.get()}\t{self.cow_price_final}")
            if self.buffalo_milk_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.buffalo.get()} Buffalo Milk \t\t\t{self.buffalo_milk_txt.get()}\t{self.c_fc_p}")
            if self.butter_milk_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.butter_milk.get()} Butter Milk \t\t\t{self.butter_milk_txt.get()}\t{self.c_fw_p}")
            if self.curd_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.curd.get()} Curd \t\t\t{self.curd_txt.get()}\t{self.c_hs_p}")
            if self.paneer_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.paneer.get()} Paneer \t\t\t{self.paneer_txt.get()}\t{self.c_hg_p}")
            if self.flav_milk.get() != 0:
                self.txtarea.insert(
                    END, f"\n Flavoured Milk \t\t\t{self.flav_milk.get()}\t{self.c_bl_p}")

            # Products2

            if self.shrikhand_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.shrikhand.get()} Shrikhand \t\t\t{self.shrikhand_txt.get()}\t{self.g_r_p}")
            if self.amrakhand_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.amrakhand.get()} Amrakhand \t\t\t{self.amrakhand_txt.get()}\t{self.g_f_p}")
            if self.cow_ghee_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.cow_ghee.get()} Cow Ghee \t\t\t{self.cow_ghee_txt.get()}\t{self.g_d_p}")
            if self.buffalo_ghee_txt.get() != 0:
                self.txtarea.insert(
                    END, f"\n {self.buffalo_ghee.get()} Buffalo Ghee \t\t\t{self.buffalo_ghee_txt.get()}\t{self.g_w_p}")
            if self.butter.get() != 0:
                self.txtarea.insert(
                    END, f"\n Butter \t\t\t{self.butter.get()}\t{self.g_s_p}")
            if self.lassi.get() != 0:
                self.txtarea.insert(
                    END, f"\n Lassi \t\t\t{self.lassi.get()}\t{self.g_t_p}")

            # Cold Drink

            if self.maza.get() != 0:
                self.txtarea.insert(
                    END, f"\n Maaza \t\t\t{self.maza.get()}\t{self.d_m_p}")
            if self.cock.get() != 0:
                self.txtarea.insert(
                    END, f"\n Cock \t\t\t{self.cock.get()}\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(
                    END, f"\n Frooti \t\t\t{self.frooti.get()}\t{self.d_f_p}")
            if self.thumsup.get() != 0:
                self.txtarea.insert(
                    END, f"\n Thums Up \t\t\t{self.thumsup.get()}\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(
                    END, f"\n Limca \t\t\t{self.limca.get()}\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(
                    END, f"\n Sprite \t\t\t{self.sprite.get()}\t{self.d_s_p}")

            self.txtarea.insert(
                END, f"\n-------------------------------------")

            if self.product_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, f"\n CGST\t\t\t{self.product_tax.get()}")

            # if self.product2_tax.get()!="Rs. 0.0":
            #	self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.product2_tax.get()}")

            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, f"\n SGST\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(
                END, f"\n-------------------------------------")

            self.txtarea.insert(
                END, f"\n Total Bill\t\t\t Rs. {self.Total_bill}")

            self.txtarea.insert(
                END, f"\n-------------------------------------")

            self.save_bill()
            self.pdf()

            conn = sql.connect(
                host="localhost",
                database="bill",
                user="root",
                password="12345"
            )
            cur = conn.cursor()
            cur.execute("insert into bill_table(bill_number, c_name, c_phone_number,email,cow,buffalo,butter_milk,curd,paneer,flav_milk,shrikhand,amrakhand,cow_ghee,buff_ghee,butter,lassi,maaza,coke,frooti,thubs_up,limica,sprite,product_price,p_tax,cold_tax,total) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.bill_no.get(),
                         self.c_name.get(),
                         self.c_phn.get(),
                         self.email.get(),
                         self.cow.get(),
                         self.buffalo.get(),
                         self.butter_milk.get(),
                         self.curd.get(),
                         self.paneer.get(),
                         self.flav_milk.get(),
                         self.shrikhand.get(),
                         self.amrakhand.get(),
                         self.cow_ghee.get(),
                         self.buffalo_ghee.get(),
                         self.butter.get(),
                         self.lassi.get(),
                         self.maza.get(),
                         self.cock.get(),
                         self.frooti.get(),
                         self.thumsup.get(),
                         self.limca.get(),
                         self.sprite.get(),
                         self.total_product_price,
                         self.p_tax,
                         self.d_tax,
                         self.Total_bill
                         ))
            conn.commit()
            conn.close()
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("dairysaipune@gmail.com", "saidairy123")
            msg = EmailMessage()
            msg['Subject'] = "PURCHASE INFO AT SAI DAIRY"
            msg['From'] = "dairysaipune@gmail.com"
            msg["To"] = self.email.get()
            msg.set_content(
                'Hey ' + self.c_name.get() + ", \nYou purchase at SAI DAIRY is successfull. \nYour bill number is: " + self.bill_no.get() +
                "\nYour bill is attached with the email."
            )
            files = ['Bill.pdf']
            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
            msg.add_attachment(file_data, maintype='application',
                               subtype='octet-stream', filename=file_name)
            server.send_message(msg)
            server.quit()

    def check(self):
        email1 = self.email.get()
        if (re.search(regex, email1)):
            return True
        else:
            return False

    def pdf(self):
        filename = "Bill.pdf"
        documentTitle = "BILL"
        Title = "## SAI DAIRY ##"
        Subtile = "Your bill details are:"
        textlines1 = ["Bill Number:" + self.bill_no.get(),
                      "Name:" + self.c_name.get(),
                      "Contact:"+self.c_phn.get(),
                      "Date:" + self.bbb]
        textlines2 = ["   Product Name" + "         " + "Quantity" + "          " + "Price",
                      "________________________________________________________",
                      
                      str(self.cow.get()) +" Cow Milk      " + "       " + str(self.cow_milk_txt.get())+
                      "               " + str(self.c_s_p),

                      str(self.buffalo.get()) + " Buffalo Milk  " + "       " + str(self.buffalo_milk_txt.get())
                       +
                      "               " + str(self.c_fc_p),

                      str(self.butter_milk.get()) + " Butter Milk   " + "       " + str(self.butter_milk_txt.get())
                        +
                      "               " + str(self.c_fw_p),

                      str(self.curd.get()) + "   Curd          " + "       " + str(self.curd_txt.get())
                        +
                      "               " + str(self.c_hs_p),

                      str(self.paneer.get()) + "   Paneer        " + "       " + str(self.paneer_txt.get())
                         +
                      "               " + str(self.c_hg_p),

                      "Flavoured Milk" + "             " +
                                            str(self.flav_milk.get()) +
                      "               " + str(self.c_bl_p),

                      str(self.shrikhand.get()) + " Shreekhand    " + "        " + str(self.shrikhand_txt.get())
                        +
                      "               " + str(self.g_r_p),

                      str(self.amrakhand.get()) + " Amrakhand     " + "        " + str(self.amrakhand_txt.get())
                        +
                      "               " + str(self.g_f_p),

                      str(self.cow_ghee.get()) + " Cow Ghee      " + "        " + str(self.cow_ghee_txt.get())
                        +
                      "               " + str(self.g_d_p),

                      str(self.buffalo_ghee.get()) + " Buffalo Ghee  " + "        " + str(self.buffalo_ghee_txt.get())
                       +
                      "               " + str(self.g_w_p),
                      "Butter        " + "             " +
                      str(self.butter.get()) +
                      "               " + str(self.g_s_p),
                      "Lassi         " + "             " +
                      str(self.lassi.get()) +
                      "               " + str(self.g_t_p),
                      "Mazaa         " + "             " +
                      str(self.maza.get()) +
                      "               " + str(self.d_m_p),
                      "Coke          " + "             " +
                      str(self.cock.get()) +
                      "               " + str(self.d_c_p),
                      "Frooti        " + "             " +
                      str(self.frooti.get()) +
                      "               " + str(self.d_f_p),
                      "Thumbs Up     " + "             " +
                      str(self.thumsup.get()) +
                      "               " + str(self.d_t_p),
                      "Limca         " + "             " +
                      str(self.limca.get()) +
                      "               " + str(self.d_l_p),
                      "Sprite        " + "             " +
                      str(self.sprite.get()) +
                      "               " + str(self.d_s_p),
                      ]
        textlines3 = ["CGST                                " + str(round(self.p_tax,2)),
                      "SGST                                " +
                      str(round(self.d_tax,2)),
                      "Total                               " + str(self.Total_bill), ]
        pdf = canvas.Canvas(filename)
        pdf.setTitle(documentTitle)
        pdf.setFont('Times-Bold', 30)
    # title fonts
        pdf.drawCentredString(290, 770, Title)
        pdf.setFont('Times-Roman', 22)
        pdf.drawCentredString(290, 720, Subtile)
        pdf.line(30, 710, 570, 710)
        text = pdf.beginText(40, 680)
        text.setFont('Courier', 16)
        for line in textlines1:
            text.textLine(line)
        pdf.drawText(text)
        pdf.line(30, 600, 570, 600)
        text2 = pdf.beginText(40, 550)
        text.setFont('Courier', 16)
        for line in textlines2:
            if "0" not in line:
                text2.textLine(line)
        pdf.drawText(text2)
        pdf.line(30, 120, 570, 120)
        text3 = pdf.beginText(40, 100)
        text.setFont('Courier', 16)
        for line in textlines3:
            text3.textLine(line)
        pdf.drawText(text3)

        pdf.save()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo(
                "saved", f"Bill {self.bill_no.get()} Successfully Saved...")
        else:
            return

    def abc(self):
        if self.cow.get() != 0:
            return self.cow.get()
        else:
            pass

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No....")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear Data...")

        # Product
        self.cow.set(0)

        self.buffalo.set(0)
        self.butter_milk.set(0)
        self.curd.set(0)
        self.paneer.set(0)
        self.flav_milk.set(0)

        # Product2

        self.shrikhand.set(0)
        self.amrakhand.set(0)
        self.cow_ghee.set(0)
        self.buffalo_ghee.set(0)
        self.butter.set(0)
        self.lassi.set(0)

        # Cold Drink

        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        # Total Product Price and Tax Variables

        self.product_price.set("")
        self.product2_price.set("")
        self.cold_drink_price.set("")

        self.product_tax.set("")
        self.product2_tax.set("")
        self.cold_drink_tax.set("")

        # Customer

        self.c_name.set("")
        self.c_phn.set("")
        self.email.set("")

        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill.set("")
        self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit..")
        if op > 0:
            self.root.destroy()

    def customer(self):
        self.root.destroy()
        import Customer

    def pay(self):
        self.root.destroy()
        import pay


root = Tk()
obj = Bill_App(root)
root.mainloop()
