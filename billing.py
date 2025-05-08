import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # from Pillow
from tkinter import ttk, messagebox
import sqlite3
import os
import time
import tempfile


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x770+0+10")
        self.root.title("Inventory Management System | Developed By Aj & Cj")
        self.root.config(bg="white")
        self.cart_list = []  # list to store cart items
        self.chk_print = 0

        # ====title====
        original_icon = Image.open("image/logo.png")
        resized_icon = original_icon.resize((50, 50), Image.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(resized_icon)

        # Title Label with logo
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#0049b7", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        #===button_logout===
        btn_logout = Button(self.root, text="Logout",command=self.logout, font=("times new roman", 15, "bold"), bg="red", cursor="hand2", width=10, height=1)
        btn_logout.place(x=1350, y=15)

        # ===clock==== (you can update the clock every second)
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        # self.update_clock()  # Update the clock

        # producrt frame

        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=6, y=110, width=450, height=630)

        pTitle = Label(ProductFrame1, text="All Products", font=(
            "goudy old style", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)

        # product search frame here
        self.var_search = StringVar()
        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2.5, y=42, width=436, height=105)

        lbl_search = Label(ProductFrame2, text="Search Product | By Name", font=(
            "times new roman", 18, "bold"), bg="white", fg="green").place(x=2, y=5)

        lbl_search = Label(ProductFrame2, text="Product Name", font=(
            "times new roman", 18, "bold"), bg="white").place(x=2, y=55)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=(
            "times new roman", 18), bg="lightyellow").place(x=165, y=59, width=150, height=24)
        btn_search = Button(ProductFrame2, text="Search", command=self.search, font=("goudy old style", 16),
                            bg="#2196f3", fg="white", cursor="hand2").place(x=325, y=59, width=100, height=25)
        btn_show_all = Button(ProductFrame2, text="Show All",command=self.show, font=("goudy old style", 16),
                              bg="#083531", fg="white", cursor="hand2").place(x=325, y=10, width=100, height=25)

        # products details frame here
        ProductFrame3 = Frame(ProductFrame1, bd=4, relief=RIDGE)
        ProductFrame3.place(x=2, y=150, width=436, height=444)

        # Scrollbars for Treeview
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)
        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=(
            "pid", "name", "price", "quantity", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("quantity", text="quantity")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"] = "headings"

        self.product_Table.column("pid", width=40)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("quantity", width=40)
        self.product_Table.column("status", width=80)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note = Label(ProductFrame1, text="Note:'Enter 0 quantity to remove product from the Cart' ", font=(
            "goudy old style", 12), anchor='w', bg="white", fg="red").pack(side=BOTTOM, fill=X)

        # customer frame here. The second frame on the screen (middle one)
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=458, y=110, width=602, height=75)
        cTitle = Label(CustomerFrame, text="Customer Details", font=(
            "goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)

        lbl_name = Label(CustomerFrame, text="Name", font=(
            "times new roman", 15), bg="white").place(x=5, y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=(
            "times new roman", 13), bg="lightyellow").place(x=72, y=36, width=180)

        lbl_contact = Label(CustomerFrame, text="Contact No.", font=(
            "times new roman", 15), bg="white").place(x=290, y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=(
            "times new roman", 13), bg="lightyellow").place(x=400, y=36, width=180)

        # cal cart frame
        Cal_Cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=458, y=190, width=602, height=398)

        # for calculator
        self.var_cal_input = StringVar()
        Cal_Frame = Frame(Cal_Cart_Frame, bd=9, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=6, width=300, height=384)

        txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=(
            'arial', 15, 'bold'), width=24, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(Cal_Frame, text='7', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            7), bd=5, width=4, pady=14, cursor="hand2").grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text='8', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            8), bd=5, width=4, pady=14, cursor="hand2").grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            9), bd=5, width=4, pady=14, cursor="hand2").grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text='+', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            '+'), bd=5, width=4, pady=14, cursor="hand2").grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            4), bd=5, width=4, pady=15, cursor="hand2").grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            5), bd=5, width=4, pady=15, cursor="hand2").grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            6), bd=5, width=4, pady=15, cursor="hand2").grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text='-', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            '-'), bd=5, width=4, pady=15, cursor="hand2").grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            1), bd=5, width=4, pady=14, cursor="hand2").grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            2), bd=5, width=4, pady=14, cursor="hand2").grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            3), bd=5, width=4, pady=14, cursor="hand2").grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text='*', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            '*'), bd=5, width=4, pady=14, cursor="hand2").grid(row=3, column=3)

        btn_c = Button(Cal_Frame, text='c', font=('araial', 17, 'bold'), command=self.clr_input,
                       bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=0)
        btn_0 = Button(Cal_Frame, text='0', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            0), bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=1)
        btn_eq = Button(Cal_Frame, text='=', font=('araial', 17, 'bold'), command=self.perform_cal,
                        bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text='/', font=('araial', 17, 'bold'), command=lambda: self.get_input(
            '/'), bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=3)

        # Cart frame
        cart_Frame = Frame(Cal_Cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=310, y=6, width=285, height=384)
        self.Cart_Title = Label(cart_Frame, text="Cart \t Total Product : [0]", font=(
            "goudy old style", 15), bg="lightgray")
        self.Cart_Title.pack(side=TOP, fill=X)

        # Scrollbars for Treeview
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)

        self.Cart_Table = ttk.Treeview(cart_Frame, columns=(
            "pid", "name", "price", "quantity"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Cart_Table.xview)
        scrolly.config(command=self.Cart_Table.yview)

        self.Cart_Table.heading("pid", text="PID")
        self.Cart_Table.heading("name", text="Name")
        self.Cart_Table.heading("price", text="Price")
        self.Cart_Table.heading("quantity", text="Qty")
        

        self.Cart_Table["show"] = "headings"

        self.Cart_Table.column("pid", width=40)
        self.Cart_Table.column("name", width=90)
        self.Cart_Table.column("price", width=90)
        self.Cart_Table.column("quantity", width=40)
        self.Cart_Table.pack(fill=BOTH, expand=1)
        self.Cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)

        # add cart widgets here
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_stock = StringVar()
        
        
        
        
        Add_CartWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=458, y=590, width=602, height=150)

        lbl_p_name = Label(Add_CartWidgetsFrame, text="Products Name", font=(
            "goudy old style", 15), bg="white").place(x=5, y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=(
            "goudy old style", 15), bg="lightyellow", state='readonly').place(x=5, y=35, width=190, height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame, text="Price Per quantity", font=(
            "goudy old style", 15), bg="white").place(x=230, y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=(
            "goudy old style", 15), bg="lightyellow", state='readonly').place(x=230, y=35, width=150, height=22)

        lbl_p_quantity = Label(Add_CartWidgetsFrame, text="quantity", font=(
            "goudy old style", 15), bg="white").place(x=390, y=5)
        txt_p_quantity = Entry(Add_CartWidgetsFrame, textvariable=self.var_quantity, font=(
            "goudy old style", 15), bg="lightyellow").place(x=390, y=35, width=120, height=22)

        self.lbl_inStock = Label(Add_CartWidgetsFrame, text="In Stock", font=(
            "goudy old style", 15), bg="white")
        self.lbl_inStock.place(x=5, y=70)

        # buttons here
        btn_clear_cart = Button(Add_CartWidgetsFrame, text="Clear",command=self.clear_cart, font=(
            "times new roman", 15, "bold"), bg="lightgray", cursor="hand2").place(x=180, y=70, width=150, height=30)
        btn_add_cart = Button(Add_CartWidgetsFrame, text="Add | Update Cart",command=self.add_update_cart, font=(
            "times new roman", 15, "bold"), bg="orange", cursor="hand2").place(x=340, y=70, width=180, height=30)

        # billing
        billFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billFrame.place(x=1062, y=110, width=450, height=478)

        BTitle = Label(billFrame, text="Customer Bill Area ", font=(
            "goudy old style", 20, "bold"), bg="#262627", fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # buttons for billing
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billMenuFrame.place(x=1062, y=590, width=450, height=150)

        self.lbl_amnt = Label(billMenuFrame, text='Bill Amount\n[0]', font=(
            "goudy old style", 15, "bold"), bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=5, y=5, width=145, height=70)

        self.lbl_discount = Label(billMenuFrame, text='Discount \n[5%]', font=(
            "goudy old style", 15, "bold"), bg="#8bc34a", fg="white")
        self.lbl_discount.place(x=155, y=5, width=135, height=70)

        self.lbl_net_pay = Label(billMenuFrame, text='Net Pay\n[0]', font=(
            "goudy old style", 15, "bold"), bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=295, y=5, width=145, height=70)

        btn_print = Button(billMenuFrame, text='Print',command=self.print_bill, cursor='hand2', font=(
            "goudy old style", 15, "bold"), bg="lightgreen", fg="white")
        btn_print.place(x=5, y=80, width=145, height=50)

        btn_clr_all = Button(billMenuFrame, text='Clear All', command=self.clear_all, cursor='hand2', font=(
            "goudy old style", 15, "bold"), bg="gray", fg="white")
        btn_clr_all.place(x=155, y=80, width=135, height=50)

        btn_generate = Button(billMenuFrame, text='Generate/Save Bill',command=self.generate_bill , cursor='hand2',
                font=("goudy old style", 14, "bold"), bg="#009688", fg="white")
        btn_generate.place(x=295, y=80, width=145, height=50)

        # footteerrr
        footer = Label(self.root, text="Inventory Management System | Developed By AJ & CJ", font=(
            "times new roman", 11), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

        self.show()
        self.update_date_time()  # Update the clock
        # self.bill_top()
        
        
    # ===========================functions here========================

    def get_input(self, num):
        xnum = self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clr_input(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select pid,Name, price, quantity,status from product where status='Active'")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror(
                    "Error", "search input should be reqired", parent=self.root)
            else:
                cur.execute(
                    "select pid, Name, Price, quantity, Status from product where Name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_Table.delete(
                        *self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])  
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3 ])}]")
        self.var_stock.set(row[3])
        self.var_quantity.set('1')
        
        
    def get_data_cart(self,ev):
        f=self.Cart_Table.focus()
        content=(self.Cart_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        
        
    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror(
                "Error", "Please select product from the list", parent=self.root)   
        elif self.var_quantity.get() == '':
            messagebox.showerror(
                "Error", "Please enter quantity", parent=self.root)
        elif int(self.var_quantity.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error', "Insufficient stock available", parent=self.root)
        else:
            # price_cal=float(int(self.var_quantity.get())*float(self.var_price.get()))
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_quantity.get(),self.var_stock.get()]
            
           #===update cart===
           
            present= 'no' 
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            
            if present=='yes':
                op=messagebox.askyesno('confirm', "product already present in cart, do you want to update | Remove from the cart",parent=self.root)
                if op==True:
                    if self.var_quantity.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_quantity.get() #quantity
                        
                        
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()
            
    def bill_update(self): 
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
            
        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amt)}')
        self.lbl_net_pay.config(text=f'Net Pay(RS.)\n{str(self.bill_amt-self.discount)}')
        self.Cart_Title.config(text=f"Cart \t Total Product : [{str(len(self.cart_list))}]") 
               
            
            
            
    def show_cart(self):
        con= sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            self.Cart_Table.delete(*self.Cart_Table.get_children())
            for row in self.cart_list:
                self.Cart_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror('Error', 'Customer details are required',parent=self.    root)
        elif len(self.cart_list)==0:
            messagebox.showerror('Error', 'Add product to the cart', parent=self.root)
        else:
            
                #====bill Top====
            self.bill_top()
                #====bill Middle====
            self.bill_middle()
                #====bill Bottom====
            self.bill_bottom()
            
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get(1.0,END))
            fp.close()
            messagebox.showinfo('Saved',f'Bill has been saved as {str(self.invoice)}.txt in bill folder',parent=self.root)
            self.chk_print=1
                
            
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp= f'''
\t\t    ABCD-Inventory 
\tMobile No. : 836810XXXX , Haryana-122003 
{str("="*53)}
 Customer Name : {self.var_cname.get()}
 Mob. No. : {self.var_contact.get()}
 Bill No. : {str(self.invoice)}\t\t\t\t   Date : {str(time.strftime("%d/%m/%Y"))}
{str("="*53)}
 Product Name\t\t\tQty\t\tPrice
{str("="*53)}
        '''
        self.txt_bill_area.delete(1.0,END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
        
    
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*53)}
 Bill Amount:\t\t\t\t\tRs.{self.bill_amt}
 Discount:\t\t\t\t\tRs.{self.discount}
 Net Pay:\t\t\t\t\tRs.{self.net_pay}
{str("="*53)}\n
\t\tThank You For Shopping!
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
    
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                else:
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\t\tRs."+price)
                # update product quantity in product table
                cur.execute('update product set quantity=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
            
    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_quantity.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete(1.0,END)
        self.Cart_Title.config(text=f"Cart \t Total Product : [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d/%m/%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(1000,self.update_date_time)
       
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print', 'please wait while printing the bill', parent=self.root)
            new_file = tempfile.mktemp('.txt')
            with open(new_file, 'w') as f:
                f.write(self.txt_bill_area.get(1.0, END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror('Error', 'Please generate the bill first', parent=self.root)
            new_file = tempfile.mktemp('.txt')
            with open(new_file, 'w') as f:
                f.write(self.txt_bill_area.get(1.0, END))
            os.startfile(new_file, 'print') 
            
    def logout(self):
       self.root.destroy()
       os.system("python login.py")       
           
            
            
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
