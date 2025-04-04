from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class employeeClass:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1310x630+212+110")
        self.root.title("EMPLOYEE_DATA_STORATION")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(True, True)

        # All variables
        
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        self.var_address = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE )
        SearchFrame.place(x=250, y=20, width=600, height=70) 

        # Option
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=6, width=160)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=6)
        
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=420, y=5, width=150, height=30)

        # Title
        title = Label(self.root, text="Employee Details", font=("goudy old style", 18), bg="#0f4d7d", fg="white").place(x=30, y=105, width=1250)
        

        # Content that would be shown in the employee details (row 1)
        lbl_empid = Label(self.root, text="Emp ID", font=("goudy old style", 15), bg="white").place(x=30, y=150)
        
        
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15), bg="white").place(x=410, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=760, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15), bg="lightyellow").place(x=140, y=150, width=210)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_gender.place(x=515, y=150, width=210)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=872, y=150, width=210)

        # Content that would be shown in the employee details (row 2)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=30, y=190)
        lbl_dob = Label(self.root, text="DOB", font=("goudy old style", 15), bg="white").place(x=410, y=190)
        lbl_doj = Label(self.root, text="DOJ", font=("goudy old style", 15), bg="white").place(x=760, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=140, y=190, width=210)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(x=515, y=190, width=210)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 15), bg="lightyellow").place(x=872, y=190, width=210)

        # Content that would be shown in the employee details (row 3)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="white").place(x=30, y=230)
        lbl_pass = Label(self.root, text="Password", font=("goudy old style", 15), bg="white").place(x=410, y=230)
        lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 15), bg="white").place(x=760, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=140, y=230, width=210)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 15), bg="lightyellow").place(x=515, y=230, width=210)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Select", "Admin", "Employee"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_utype.place(x=872, y=230, width=210)
        cmb_utype.current(0)

        # Content that would be shown in the employee details (row 4)
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=30, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="white").place(x=760, y=270)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=140, y=270, width=330, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 15), bg="lightyellow").place(x=872, y=270, width=210)

        # Buttons (Save, Update, Delete)
        btn_save = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=500, y=305, width=120, height=28)
        btn_update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=630, y=305, width=120, height=28)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=760, y=305, width=120, height=28)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=890, y=305, width=120, height=28)
        
       ##Employee Details==
       
        # Frame for seeing employee details as spreadsheets
        emp_frame = Frame(self.root, bd=4, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=275)

        # To scroll data if it is too vast or big
        scrollX = Scrollbar(emp_frame, orient=HORIZONTAL)
        scrollY = Scrollbar(emp_frame, orient=VERTICAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("Empid", "Name", "Email", "Gender", "Contact", "DOB", "DOJ", "Pass", "Utype", "Address", "Salary"), yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.EmployeeTable.xview)
        scrollY.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("Empid", text="EMP ID")
        self.EmployeeTable.heading("Name", text="NAME")
        self.EmployeeTable.heading("Email", text="EMAIL")
        self.EmployeeTable.heading("Gender", text="GENDER")
        self.EmployeeTable.heading("Contact", text="CONTACT")
        self.EmployeeTable.heading("DOB", text="DOB")
        self.EmployeeTable.heading("DOJ", text="DOJ")
        self.EmployeeTable.heading("Pass", text="PASSWORD")
        self.EmployeeTable.heading("Utype", text="USER TYPE")
        self.EmployeeTable.heading("Address", text="ADDRESS")
        self.EmployeeTable.heading("Salary", text="SALARY")

        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.column("Empid", width=90)
        self.EmployeeTable.column("Name", width=100)
        self.EmployeeTable.column("Email", width=200)
        self.EmployeeTable.column("Gender", width=90)
        self.EmployeeTable.column("Contact", width=100)
        self.EmployeeTable.column("DOB", width=100)
        self.EmployeeTable.column("DOJ", width=100)
        self.EmployeeTable.column("Pass", width=100)
        self.EmployeeTable.column("Utype", width=100)
        self.EmployeeTable.column("Address", width=250,)
        self.EmployeeTable.column("Salary", width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)  
        
        self.show()

#==================================================================        
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":  # Check for missing Empid
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE Empid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row:  # If employee with that ID already exists
                    messagebox.showerror("Error", "This Employee ID already exists, try different", parent=self.root)
                else:
                    # Inserting new employee record
                    cur.execute("INSERT INTO employee(Empid, Name, Email, Gender, Contact, DOB, DOJ, Pass, Utype, Address, Salary) VALUES(?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_emp_id.get(),
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
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select* from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
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
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
            if not rows:
                messagebox.showinfo("Info", "No records found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
            

if __name__ == "__main__":  
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
