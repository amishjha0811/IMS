import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # from Pillow
from time import strftime

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x770+0+0")
        self.root.title("Inventory Management System | Developed By Aj & Cj")
        self.root.config(bg="#f0f0f0")  # Light background for modern look
        
        # Title
        original_icon = Image.open("image/logo.png")  
        resized_icon = original_icon.resize((50, 50), Image.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(resized_icon)
        
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("Helvetica Neue", 40, "bold"), bg="#0049b7", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        # Logout Button
        btn_logout = Button(self.root, text="Logout", font=("Helvetica Neue", 15, "bold"), bg="#ff4d4d", cursor="hand2", width=10, height=1)
        btn_logout.place(x=1350, y=15)
        
        # Clock
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("Helvetica Neue", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()  # Update the clock
        
        # Left Menu
        self.MenuLogo = Image.open("image/logo2.jpg")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=658)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        # Menu label
        lbl_menu = Label(LeftMenu, text="Menu", font=("Helvetica Neue", 20), bg="#009688", fg="white")
        lbl_menu.pack(side=TOP, fill=X)
        
        # Menu Buttons
        self.create_menu_button(LeftMenu, "Employee", self.show_employee)
        self.create_menu_button(LeftMenu, "Supplier", self.show_supplier)
        self.create_menu_button(LeftMenu, "Category", self.show_category)
        self.create_menu_button(LeftMenu, "Product", self.show_product)
        self.create_menu_button(LeftMenu, "Sales", self.show_sales)
        self.create_menu_button(LeftMenu, "Exit", self.exit_application)
        
        # Content Labels
        self.lbl_employee = Label(self.root, text="Total Employee\n [0]", relief=RIDGE, bd=5, bg="#ffdd00", fg="black", font=("Helvetica Neue", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)
        
        self.lbl_supplier = Label(self.root, text="Total Supplier\n [0]", relief=RIDGE, bd=5, bg="#ff7d00", fg="black", font=("Helvetica Neue", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)
        
        self.lbl_category = Label(self.root, text="Total Category\n [0]", relief=RIDGE, bd=5, bg="#ff006d", fg="black", font=("Helvetica Neue", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)
        
        self.lbl_product = Label(self.root, text="Total Product\n [0]", relief=RIDGE, bd=5, bg="#8f00ff", fg="black", font=("Helvetica Neue", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)
        
        self.lbl_sales = Label(self.root, text="Total Sales\n [0]", relief=RIDGE, bd=5, bg="#ffb3ae", fg="black", font=("Helvetica Neue", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        
        # Footer
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | Developed By Aj & Cj\nFor any Technical Issue Contact: 8368xxxx12",
                           font=("Helvetica Neue", 12), bg="#20263e", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)

    def create_menu_button(self, parent, text, command):
        button = Button(parent, text=text, font=("Helvetica Neue", 20, "bold"), bg="#009688", fg="white", bd=0, cursor="hand2", command=command)
        button.pack(side=TOP, fill=X, padx=5, pady=5)
        button.bind("<Enter>", lambda e: button.config(bg="#00796b"))
        button.bind("<Leave>", lambda e: button.config(bg="#009688"))

    def update_clock(self):
        time_string = strftime('%H:%M:%S')
        date_string = strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {date_string}\t\t Time: {time_string}")
        self.lbl_clock.after(1000, self.update_clock)  # Update every 1000ms (1 second)

    def show_employee(self):
        print("Employee button clicked!")

    def show_supplier(self):
        print("Supplier button clicked!")

    def show_category(self):
        print("Category button clicked!")

    def show_product(self):
        print("Product button clicked!")

    def show_sales(self):
        print("Sales button clicked!")

    def exit_application(self):
        self.root.quit()

# Create the Tkinter root window
root = Tk()

# Initialize the IMS class
obj = IMS(root)

# Start the Tkinter event loop
root.mainloop()