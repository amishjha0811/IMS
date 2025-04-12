import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # from Pillow
from tkinter import ttk,messagebox
import os


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x770+0+10")
        self.root.title("Inventory Management System | Developed By Aj & Cj")
        self.root.config(bg="white")
        
        #====title====
        original_icon = Image.open("image/logo.png")  
        resized_icon = original_icon.resize((50, 50), Image.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(resized_icon)
        
        # Title Label with logo
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#0049b7", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        #===button_logout===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="red", cursor="hand2", width=10, height=1)
        btn_logout.place(x=1350, y=15)
        
        #===clock==== (you can update the clock every second)
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
        font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        #self.update_clock()  # Update the clock
        # producrt frame
        self.var_search=StringVar()
        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        
        pTitle=Label(ProductFrame1,text="All Products",font=("goudy ols style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_name=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        lxt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        ProductFrame3 = Frame(ProductFrame1,bd=4,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=395,height=380)

        # Scrollbars for Treeview
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)
        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid","name", "price", "qty","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="QTY")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"] = "headings"
        
        
        self.product_Table.column("pid", width=90)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=100)
        self.product_Table.column("status", width=100)
        self.product_Table.pack(fill=BOTH, expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 Quantity to remove product from the Cart' ",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()