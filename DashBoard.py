import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # from Pillow
from employee import employeeClass
from category import categoryClass
from supplier import SupplierClass
from product import productClass
from sales import salesClass


class IMS:
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
        self.update_clock()  # Update the clock
        
        #====left menu====
        self.MenuLogo = Image.open("image/logo2.jpg")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=658)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X) 
        
        # Menu label
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)
        
        
        
        btn_employee = Button(LeftMenu, text="Employee", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_employee)
        btn_employee.pack(side=TOP, fill=X)
         
        btn_supplier = Button(LeftMenu, text="Supplier", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_supplier)
        btn_supplier.pack(side=TOP, fill=X)
        
        btn_category = Button(LeftMenu, text="Category", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_category)
        btn_category.pack(side=TOP, fill=X) 
        
        btn_product = Button(LeftMenu, text="Product", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_product)
        btn_product.pack(side=TOP, fill=X) 
        
        btn_sales = Button(LeftMenu, text="Sales", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_sales)
        btn_sales.pack(side=TOP, fill=X) 
        
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2")
        btn_exit.pack(side=TOP, fill=X)
        
        #====content==
        self.lbl_employee = Label(self.root, text="Total Employee\n [0]", relief=RIDGE, bd=5, bg="#ffdd00", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)
        
        self.lbl_supplier = Label(self.root, text="Total Supplier\n [0]", relief=RIDGE, bd=5, bg="#ff7d00", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)
        
        self.lbl_category = Label(self.root, text="Total Category\n [0]", relief=RIDGE, bd=5, bg="#ff006d", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)
        
        self.lbl_product = Label(self.root, text="Total Product\n [0]", relief=RIDGE, bd=5, bg="#8f00ff", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)
        
        self.lbl_sales = Label(self.root, text="Total Sales\n [0]", relief=RIDGE, bd=5, bg="#ffb3ae", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        
        #====footer==
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | Developed By Aj & Cj\nFor any Technical Issue Contact: 8368xxxx12",
                           font=("times new roman", 12), bg="#20263e", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)
    
    
    def open_employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
    
    def open_supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)
    
    def open_category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
    
    def open_product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
        
    def open_sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)
    
    
    
    def update_clock(self):
        from time import strftime
        time_string = strftime('%H:%M:%S')
        date_string = strftime('%d-%m-%Y')
        
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {date_string}\t\t Time: {time_string}")
        self.lbl_clock.after(1000, self.update_clock) 

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

