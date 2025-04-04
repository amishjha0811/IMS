from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3


class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1310x630+212+110")
        # self.root.geometry("1100x500+220+130")
        self.root.title("Supplier Management")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_searchtxt = StringVar()
        
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
    
    
        # Search frame
        SearchFrame = LabelFrame(self.root, text="Invoice No.", bg='white', font=("goudy old style", 15))
        SearchFrame.place(x=700, y=50, width=380, height=60)  # Adjusting placement

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=10, y=1, width=252)  # Adjusting placement for search box

        btn_search = Button(SearchFrame, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white", command=self.search)
        btn_search.place(x=270, y=-7, width=100, height=35)  # Adjusting placement for search button


        # TITLE
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X, padx=5, pady=5)
        
        #==images===
        self.im1=Image.open("image/supplier.png")
        self.im1=self.im1.resize((620,210),Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=50, y=50)

        # Supplier Details (Row 1)
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50, y=280)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=280, width=180)

        # Supplier Details (Row 2)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=320)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=320, width=180)

        # Supplier Details (Row 3)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=360)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=360, width=180)

        # Supplier Details (Row 4)
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=400)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=400, width=470, height=90)

        # Buttons (add, update, delete, clear)
        btn_add = Button(self.root, text="Add", font=("goudy old style", 15), bg="#2196f3", fg="white", command=self.add).place(x=180, y=540, width=120, height=35)
        btn_update = Button(self.root, text="Update", font=("goudy old style", 15), bg="#4caf50", fg="white", command=self.update).place(x=310, y=540, width=120, height=35)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15), bg="#f44336", fg="white", command=self.delete).place(x=440, y=540, width=120, height=35)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15), bg="#607d8b", fg="white", command=self.clear).place(x=570, y=540, width=120, height=35)

        # Frame for showing supplier details
        emp_frame = Frame(self.root, bd=4, relief=RIDGE)
        emp_frame.place(x=700, y=120, width=600, height=500)

        # Scrollbars for Treeview
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        self.supplierTable["show"] = "headings"
        
        
        self.supplierTable.column("invoice", width=20)
        self.supplierTable.column("name", width=60)
        self.supplierTable.column("contact", width=70)
        self.supplierTable.column("desc", width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()   
#========================================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice No. already exists.", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) VALUES (?, ?, ?, ?)", (
                        self.var_sup_invoice.get(), 
                        self.var_name.get(), 
                        self.var_contact.get(), 
                        self.txt_desc.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully.", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invoice No. not found.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?", (
                        self.var_name.get(), 
                        self.var_contact.get(), 
                        self.txt_desc.get("1.0", END), 
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully.", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if not self.var_sup_invoice.get():
                messagebox.showerror("Error", "Invoice No. must be required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invoice No. not found.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier deleted successfully.", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
