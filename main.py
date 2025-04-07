import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # from Pillow
from Employee import employeeClass
from supplier import supplierClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x770+0+0")
        self.root.title("Inventory Management System | Developed By Aj & Cj")
        self.root.config(bg="white")
        
        #====title====
        try:
            original_icon = Image.open("image/logo.png")  
            resized_icon = original_icon.resize((50, 50), Image.LANCZOS)
            self.icon_title = ImageTk.PhotoImage(resized_icon)
        except:
            self.icon_title = None  # If the image is missing, avoid crashing

        title = Label(self.root, text="Inventory Management System", 
                      image=self.icon_title, compound=LEFT if self.icon_title else None,
                      font=("times new roman", 40, "bold"), bg="#0049b7", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        #===button_logout===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="red", cursor="hand2", width=10, height=1)
        btn_logout.place(x=1350, y=15)
        
        #===clock====
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()
        
        #====left menu====
        try:
            self.MenuLogo = Image.open("image/logo2.jpg")
            self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
            self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        except:
            self.MenuLogo = None  # Avoid errors if image is missing

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=658)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X) if self.MenuLogo else None  # Only display if image is loaded
        
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)
        
        # Menu buttons
        btn_employee = Button(LeftMenu, text="Employee", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_employee_dashboard)
        btn_employee.pack(side=TOP, fill=X)
        
        btn_supplier = Button(LeftMenu, text="Supplier", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.open_supplier_dashboard)
        btn_supplier.pack(side=TOP, fill=X)
        
        btn_category = Button(LeftMenu, text="Category", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X) 
        
        btn_product = Button(LeftMenu, text="Product", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X) 
        
        btn_sales = Button(LeftMenu, text="Sales", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X) 
        
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="skyblue", bd=3, cursor="hand2", command=self.root.quit)
        btn_exit.pack(side=TOP, fill=X)
        
    def open_supplier_dashboard(self):
        try:
            import supplier_dashboard  # Ensure supplier_dashboard.py exists
            new_win = Toplevel(self.root)
            supplier_dashboard.SupplierClass(new_win)
        except ImportError:
            print("Error: supplier_dashboard.py not found.")

    def open_employee_dashboard(self):
        try:
          # Ensure employeeClass.py exists
            new_win = Toplevel(self.root)
            employeeClass.employeeClass(new_win)
        except ImportError:
            print("Error: employeeClass.py not found.")

    def update_clock(self):
        from time import strftime
        time_string = strftime('%H:%M:%S')
        date_string = strftime('%d-%m-%Y')
        
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {date_string}\t\t Time: {time_string}")
        self.lbl_clock.after(1000, self.update_clock)  # Update every 1000ms (1 second)

# Create the Tkinter root window
root = Tk()

# Initialize the IMS class
obj = IMS(root)

# Start the Tkinter event loop
root.mainloop()
