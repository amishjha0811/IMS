from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class salesClass:
    
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1310x630+212+110")
        self.root.title("Sales Management")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.bill_list=[]
        self.var_invoice=StringVar()
        
        # Title
        lbl_title = Label(self.root, text="View Customer Bills", font=("goudy old style", 30), 
        bg="#184a45", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 18), 
        bg="white", )
        lbl_invoice.place(x=50, y=120)
        
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), 
        bg="lightgray", )
        txt_invoice.place(x=180, y=120, width=200, height=31)
        
        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 18, "bold"), bg="darkblue", fg="white",cursor="hand2").place(x=400, y=120, width=150, height=30)
        
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("times new roman", 18, "bold"), bg="gray",cursor="hand2").place(x=570, y=120, width=150, height=30)
        
        #=======Bill List==========
        sales_Frame=Frame(self.root, bd=3,relief=RIDGE)
        sales_Frame.place(x=50, y=180, width=220, height=420)
        
        scrolly=Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame, font=("goudy old style",18), 
        bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
        
        #=======Bill Area==========
        bill_Frame=Frame(self.root, bd=3,relief=RIDGE)
        bill_Frame.place(x=300, y=180, width=500, height=420)
        
        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("goudy old style", 20), 
        bg="#FCBE6A")
        lbl_title2.pack(side=TOP, fill=X)
        
        scrolly2=Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area=Text(bill_Frame, font=("goudy old style",18), 
        bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)
        
        #====image=-=-=-==
        self.bill_photo = Image.open("image/cat2.jpg")
        self.bill_photo = self.bill_photo.resize((480, 330), Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image=Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=820, y=210)
        
        self.show()
        #------------------------------------------------
    def show(self):
        self.bill_list[:]
        self.Sales_List.delete(0,END)
        # print(os.listdir('../IMS'))  bill1.txt, category.py, 
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                
    def get_data(self, ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
        
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be reqired",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                # print("yes find the invoice")
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)

    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)    

if __name__ == "__main__":  
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
