from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3
class categoryClass:
    def __init__(self, root):  # Fixed the constructor method name
        self.root = root
        self.root.geometry("1310x630+212+110")
        # self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By Aj & Cj")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #===variables==
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        #title
        
        lbl_title=Label(self.root,text="Manage product category",font=("goudy old style",30),bg="#184a45",fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white",).place(x=50, y=100,)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow",).place(x=50, y=170, width=300)
        
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="green", fg="white", cursor="hand2").place(x=360, y=170, width=150, height=30)
        
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="red", fg="white", cursor="hand2").place(x=520, y=170, width=150, height=30)
        
        
        #=====Category Details=====
        
        cat_frame = Frame(self.root, bd=4, relief=RIDGE)
        cat_frame.place(x=700, y=100, width=380, height=100)
        
        scrollX = Scrollbar(cat_frame, orient=HORIZONTAL)
        scrollY = Scrollbar(cat_frame, orient=VERTICAL)

        self.category_table = ttk.Treeview(cat_frame, columns=("cid", "Name"),yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.category_table.xview)
        scrollY.config(command=self.category_table.yview)

        self.category_table.heading("cid", text="C ID")
        self.category_table.heading("Name", text="Name")
       
        self.category_table["show"] = "headings"
        self.category_table.column("cid", width=90)
        self.category_table.column("Name", width=100)
        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)
        
        
        #==images===
        self.im1=Image.open("image/cat.jpg")
        self.im1=self.im1.resize((500,250),Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=50, y=220)
        
        
        self.im2=Image.open("image/category.jpg")
        self.im2=self.im2.resize((500,250),Image.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2=Label(self.root,image=self.im2, bd=2, relief=RAISED)
        self.lbl_im2.place(x=580, y=220)
        
        self.show()
        
        
        #====functions==-======
         
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get() == "":  # Check for missing Category
                messagebox.showerror("Error", "Category name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row !=None:  # If Category with that ID already exists
                    messagebox.showerror("Error", "Category already present, try different", parent=self.root)
                else:
                    # Inserting new Category record
                    cur.execute("INSERT INTO category(name) VALUES(?)", (
                        self.var_name.get(), 
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select* from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
              
    def get_data(self,ev):
        f = self.category_table.focus()
        content = self.category_table.item(f)
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
      
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":  # Check for missing invoice
                messagebox.showerror("Error", "please select category from  the list", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Error,please try again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                      con.commit()
                      messagebox.showinfo("delete","category Deleted successfully",parent=self.root)
                      self.show()
                      self.var_cat_id.set("")
                      self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
           
        
if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()       
