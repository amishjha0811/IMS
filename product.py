from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class productClass:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1310x630+212+110")
        self.root.title("PRODUCT MANAGEMENT")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #################################
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.category_list=[]
        self.sup_list=[]
        self.fetch_category_sup()
        
        self.var_category=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=530,height=610)  
        
         # column1
         
        title = Label(product_Frame, text="Manage Products Details", font=("goudy old style", 20), bg="brown", fg="white").pack(side=TOP,fill=X)
        
        lbl_category = Label(product_Frame, text="Category", font=("goudy old style", 20), bg="white", fg="black").place(x=30,y=60)
        
        lbl_Supplier = Label(product_Frame, text="Supplier", font=("goudy old style", 20), bg="white", fg="black").place(x=30,y=120)
        
        lbl_Product_Name = Label(product_Frame, text="Name", font=("goudy old style", 20), bg="white", fg="black").place(x=30,y=180)
        
        lbl_Price = Label(product_Frame, text="Price", font=("goudy old style", 20), bg="white", fg="black").place(x=30,y=240)
        
        lbl_qty = Label(product_Frame, text="Quantity", font=("goudy old style", 20), bg="white", fg="black").place(x=30,y=300)
        
        lbl_Status = Label(product_Frame, text="Status", font=("goudy old style", 20), bg="white", fg="black").place(x=30,y=360)
        
        
        
        
        ##column2#########
        cmb_category = ttk.Combobox(product_Frame, textvariable=self.var_category, values=self.category_list, state="readonly", justify=CENTER, font=("goudy old style", 18))
        cmb_category.place(x=150,y=60,width=250)
        cmb_category.current(0)
        
        cmb_supplier = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state="readonly", justify=CENTER, font=("goudy old style", 18))
        cmb_supplier.place(x=150,y=120,width=250)
        cmb_supplier.current(0)
        
        txt_name =Entry(product_Frame, textvariable=self.var_name,font=("goudy old style", 18),bg='lightyellow').place(x=150,y=180,width=250)
        txt_price =Entry(product_Frame, textvariable=self.var_price,font=("goudy old style", 18),bg='lightyellow').place(x=150,y=240,width=250)
        txt_qty =Entry(product_Frame, textvariable=self.var_qty,font=("goudy old style", 18),bg='lightyellow').place(x=150,y=300,width=250)
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active","Inactive"), state="readonly", justify=CENTER, font=("goudy old style", 18))
        cmb_status.place(x=150,y=360,width=250)
        cmb_status.current(0)
        
        btn_save = Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15), bg="darkblue", fg="white").place(x=10, y=500, width=120, height=40)
        btn_update = Button(product_Frame, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=140, y=500, width=120, height=40)
        btn_delete = Button(product_Frame, text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=270, y=500, width=120, height=40)
        btn_clear = Button(product_Frame, text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=400, y=500, width=120, height=40)
        
        
        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style", 15, "bold"), bd=2, relief=RIDGE )
        SearchFrame.place(x=560, y=10, width=720, height=80) 

        # Option
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Catagory", "Supplier", "Name"), state="readonly", justify=CENTER, font=("goudy old style", 18))
        cmb_search.place(x=10, y=6, width=250)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 18), bg="lightyellow").place(x=280, y=6, width=230)
        
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 18), bg="#4caf50", fg="white").place(x=530, y=5, width=170, height=30)

        
        
     #=======#Product Details=======================
       
        # Frame for seeing employee details as spreadsheets
        p_Frame = Frame(self.root, bd=5, relief=RIDGE)
        p_Frame.place(x=560, y=100, width=720, height=520)

        # To scroll data if it is too vast or big
        scrollX = Scrollbar(p_Frame, orient=HORIZONTAL)
        scrollY = Scrollbar(p_Frame, orient=VERTICAL)

        self.product_table = ttk.Treeview(p_Frame, columns=("Pid", "Supplier","Category", "Name", "Price", "Quantity", "Status"), 
        yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.product_table.xview)
        scrollY.config(command=self.product_table.yview)

        self.product_table.heading("Pid", text="P id")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("Name", text="Name")
        self.product_table.heading("Price", text="Price")
        self.product_table.heading("Quantity", text="Quantity")
        self.product_table.heading("Status", text="Status")
        
        self.product_table["show"] = "headings"
        self.product_table.column("Pid", width=50)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier", width=70)
        self.product_table.column("Name", width=150)
        self.product_table.column("Price", width=100)
        self.product_table.column("Quantity", width=60)
        self.product_table.column("Status", width=60)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)  
        
        self.show()
        
        
        #================================================================== 
    def fetch_category_sup(self):
        self.category_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            category=cur.fetchall()
            if len(category)>0:
                del self.category_list[:]
                self.category_list.append("select")
                for i in category:
                    self.category_list.append(i[0])
            
            cur.execute("SELECT name FROM supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("select")
                for i in sup:
                    self.sup_list.append(i[0])
            
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
                
               
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            
            if self.var_category.get() == "Select" or self.var_category.get() == "Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":  
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE Name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row:  # If employee with that ID already exists
                    messagebox.showerror("Error", "Product already Present, try different", parent=self.root)
                else:
                    # Inserting new employee record
                    cur.execute("INSERT INTO product(Category, Supplier, Name, Price, Quantity, Status) VALUES(?,?,?,?,?,?)", (
                        self.var_category.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "product Added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select* from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values'] 
        
        
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END),
        self.txt_address.insert( END,row[9])
        self.var_salary.set(row[10])

    
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":  # Check for missing Empid
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE Empid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID",parent=self.root)
                else:
                    # Inserting new employee record
                    cur.execute("Update employee set Name=?, Email=?, Gender=?, Contact=?, DOB=?, DOJ=?, Pass=?, Utype=?, Address=?, Salary=? where Empid=?", (

                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated successfully", parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":  # Check for missing Empid
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE Empid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID, try different", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from employee where Empid=?",(self.var_emp_id.get(),))
                      con.commit()
                      messagebox.showinfo("delete","Employee Deleted successfully",parent=self.root)
                      self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def clear(self):    
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END),
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
        
        
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="select" or self.var_searchtxt.get() == "":
                messagebox.showerror("Error","select search a search option or enter a search term",parent=self.root)
                return
                
            query = f"SELECT * FROM employee WHERE {self.var_searchby.get()} LIKE ?"
            cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
            if not rows:
                messagebox.showinfo("Info", "No records found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
                   
if __name__ == "__main__":  
    root = Tk()
    obj = productClass(root)
    root.mainloop()
