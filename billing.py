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
        
        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #product search frame here
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        # products details frame here
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

        # customer frame here. The second frame on the screen (middle one)
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=72,y=36,width=180)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=265,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=372,y=36,width=140)
       
        #cal cart frame
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
        
        # for calculator
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state="readonly")
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text='7',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text='1',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('araial',15,'bold'),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=3)

        btn_c=Button(Cal_Frame,text='c',font=('araial',15,'bold'),bd=5,width=4,pady=10.5,cursor="hand2").grid(row=4,column=0)
        btn_0=Button(Cal_Frame,text='0',font=('araial',15,'bold'),bd=5,width=4,pady=10.5,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('araial',15,'bold'),bd=5,width=4,pady=10.5,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('araial',15,'bold'),bd=5,width=4,pady=10.5,cursor="hand2").grid(row=4,column=3)

                
        # Cart frame 
        cart_Frame = Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)
        Cart_Title=Label(cart_Frame,text="Cart \t Total : [0]",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        # Scrollbars for Treeview
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)

        self.Cart_Table = ttk.Treeview(cart_Frame, columns=("pid","name", "price", "qty","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Cart_Table.xview)
        scrolly.config(command=self.Cart_Table.yview)

        self.Cart_Table.heading("pid", text="PID")
        self.Cart_Table.heading("name", text="Name")
        self.Cart_Table.heading("price", text="Price")
        self.Cart_Table.heading("qty", text="QTY")
        self.Cart_Table.heading("status", text="Status")

        self.Cart_Table["show"] = "headings"
        
        
        self.Cart_Table.column("pid", width=40)
        self.Cart_Table.column("name", width=100)
        self.Cart_Table.column("price", width=90)
        self.Cart_Table.column("qty", width=40)
        self.Cart_Table.column("status", width=90)
        self.Cart_Table.pack(fill=BOTH, expand=1)
        #self.Cart_Table.bind("<ButtonRelease-1>",self.get_data)
        
        # add cart widgets heree
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Products Name",font=("goudy old style",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("goudy old style",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("goudy old style",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("goudy old style",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock [9999]",font=("goudy old style",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        #buttons here
        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)


if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
