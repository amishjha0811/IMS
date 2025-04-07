from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import sqlite3

class supplierClass:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Supplier Management")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Variables
        self.var_searchtxt = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        
        # Database connection
        self.conn = sqlite3.connect("suppliers.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Search Frame
        lbl_search = Label(self.root, text="Invoice No.", bg='white', font=("goudy old style", 15))
        lbl_search.place(x=700, y=80)
        
        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=800, y=80, width=172)
        
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white", command=self.search)
        btn_search.place(x=980, y=80, width=100, height=27)
        
        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=50, y=10, width=1000, height=40)
        
        # Supplier Details
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white")
        lbl_supplier_invoice.place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow")
        txt_supplier_invoice.place(x=180, y=80, width=180)
        
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=180, y=120, width=180)
        
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=50, y=160)        
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow")
        txt_contact.place(x=180, y=160, width=180)
        
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white")
        lbl_desc.place(x=50, y=200)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=470, height=90)
        
        # Buttons
        btn_save = Button(self.root, text="Save", font=("goudy old style", 15), bg="#2196f3", fg="white", command=self.add)
        btn_save.place(x=180, y=340, width=120, height=35)
        
        btn_update = Button(self.root, text="Update", font=("goudy old style", 15), bg="#4caf50", fg="white", command=self.update)
        btn_update.place(x=310, y=340, width=120, height=35)
        
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15), bg="#f44336", fg="white", command=self.delete)
        btn_delete.place(x=440, y=340, width=120, height=35)
        
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15), bg="#607d8b", fg="white", command=self.clear)
        btn_clear.place(x=570, y=340, width=120, height=35)
        
        # Supplier Table
        emp_frame = Frame(self.root, bd=4, relief=RIDGE)
        emp_frame.place(x=700, y=120, width=380, height=350)
        
        scrollX = Scrollbar(emp_frame, orient=HORIZONTAL)
        scrollY = Scrollbar(emp_frame, orient=VERTICAL)
        
        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "Name", "contact", "desc"), yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.supplierTable.xview)
        scrollY.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("Name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        
        self.supplierTable["show"] = "headings"
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("Name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        
        self.show()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers(
                            invoice_no TEXT PRIMARY KEY,
                            name TEXT,
                            contact TEXT,
                            description TEXT)''')
        self.conn.commit()

    def add(self):
        if not self.var_sup_invoice.get() or not self.var_name.get() or not self.var_contact.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                self.cursor.execute("INSERT INTO suppliers (invoice_no, name, contact, description) VALUES (?, ?, ?, ?)", 
                                    (self.var_sup_invoice.get(), self.var_name.get(), self.var_contact.get(), self.txt_desc.get("1.0", "end-1c")))
                self.conn.commit()
                messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                self.clear()
                self.show()
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.root)

    def update(self):
        if not self.var_sup_invoice.get() or not self.var_name.get() or not self.var_contact.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                self.cursor.execute("UPDATE suppliers SET name=?, contact=?, description=? WHERE invoice_no=?", 
                                    (self.var_name.get(), self.var_contact.get(), self.txt_desc.get("1.0", "end-1c"), self.var_sup_invoice.get()))
                self.conn.commit()
                messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                self.clear()
                self.show()
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.root)

    def delete(self):
        if not self.var_sup_invoice.get():
            messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
        else:
            try:
                self.cursor.execute("DELETE FROM suppliers WHERE invoice_no=?", (self.var_sup_invoice.get(),))
                self.conn.commit()
                messagebox.showinfo("Success", "Supplier deleted successfully", parent=self.root)
                self.clear()
                self.show()
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.root)

    def search(self):
        search_value = self.var_searchtxt.get()
        self.cursor.execute("SELECT * FROM suppliers WHERE invoice_no LIKE ?", ('%' + search_value + '%',))
        rows = self.cursor.fetchall()
        if rows:
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', 'end', values=row)
        else:
            messagebox.showinfo("No Result", "No supplier found with this Invoice No.", parent=self.root)

    def show(self):
        self.cursor.execute("SELECT * FROM suppliers")
        rows = self.cursor.fetchall()
        if rows:
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', 'end', values=row)
    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete("1.0", END)
        self.var_searchtxt.set("")

    def get_data(self, event):
        selected_row = self.supplierTable.focus()
        data = self.supplierTable.item(selected_row)
        record = data['values']
        self.var_sup_invoice.set(record[0])
        self.var_name.set(record[1])
        self.var_contact.set(record[2])
        self.txt_desc.delete("1.0", END)
        self.txt_desc.insert("1.0", record[3])

if __name__ == "_main_":  
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()