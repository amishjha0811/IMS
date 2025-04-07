import email
from tkinter import*
from PIL import ImageTk 
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login System | Developed by AJ & CJ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        self.otp=''
    #imagessss
        self.phone_image=ImageTk.PhotoImage(file="image/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)
    
    #login here
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
    
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        # for employee_id frame
        lbl_user=Label(login_frame,text="Employee Id",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.employee_id=StringVar()
        self.password=StringVar()
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        # for password frame
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        #btn for login
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white").place(x=50,y=300,width=250,height=35)
        # for forget password option
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_pass,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)
        # images on display
        self.im1=ImageTk.PhotoImage(file="image/im1.png")
        self.im2=ImageTk.PhotoImage(file="image/im2.png")
        self.im3=ImageTk.PhotoImage(file="image/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
        self.ani()
        
    def ani(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.ani)
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error!","All fields are required",parent=self.root)
            else:
                cur.execute("select Utype from employee where Empid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error!","Invalid Username/Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python DashBoard.py")
                    else:
                        self.root.destroy()
                        os.system("python category.py")
                        
        except Exception as ex:
            messagebox.showerror("Error!",f"Error due to: {str(ex)}",parent=self.root)
    def forget_pass(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error!","Employee Id is required",parent=self.root)
            else:
                cur.execute("select Email from employee where Empid=?",(self.employee_id.get(),))
                Email=cur.fetchone()
                if Email==None:
                    messagebox.showerror("Error!","Invalid Employee Id",parent=self.root)
                else:
                    #forget passsssswwworddd dash
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    #call send email function
                    chk=self.email_send(Email[0])
                    if chk!="s":
                        messagebox.showerror("Error","Connection Lost,Try Again",parent=self.root)
                    else:
                        
                        self.forget_pass=Toplevel(self.root)
                        self.forget_pass.title('RESET PASSWORD')
                        self.forget_pass.geometry('400x350+500+100')
                        self.forget_pass.focus_force()

                        #for entring the OTP 
                        title=Label(self.forget_pass,text='Reset Password',font=('goudy old',15,'bold'),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_pass,text="Enter OTP received on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_pass,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=24,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forget_pass,text="SUBMIT",command=self.validate,font=("times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)
                        # for new pass n confo pass
                        new_pass=Label(self.forget_pass,text='New Password',font=('times new roman',15)).place(x=24,y=135)
                        txt_new_pass=Entry(self.forget_pass,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=24,y=175,width=250,height=30)

                        conf_pass=Label(self.forget_pass,text='Confirm Password',font=('times new roman',15)).place(x=24,y=215)
                        txt_conf_pass=Entry(self.forget_pass,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=24,y=255,width=250,height=30)

                        self.btn_new_pass=Button(self.forget_pass,text="UPDATE",command=self.update(),state=DISABLED,font=("times new roman",15),bg="lightblue")
                        self.btn_new_pass.place(x=150,y=300,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error!",f"Error due to: {str(ex)}",parent=self.root)
    
    def email_send(self,to_):
        sm=smtplib.SMTP('smtp.gmail.com',587)
        sm.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        sm.login(email_,pass_)
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        subj='Password reset OTP'
        msg=f'Dear Sir/Mam,\n\nThe OTP for password reset is {str(self.otp)}.\n\nWith Regards,\n AJ N CJ'
        msg="Subject:{}\n\n{}".format(subj,msg)
        sm.sendmail(email_,to_,msg)
        chk=sm.ehlo()
        if chk[0]==250:
            return "sucess"
        else:
            return "failed"
        
    def validate(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_new_pass.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error!","Invalid OTP!",parent=self.forget_pass)
    
    def update(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error!","Password is required.",parent=self.forget_pass)
        elif self.var_new_pass.get()!="" or self.var_conf_pass.get():
            messagebox.showerror("Error!","The New & Confirm password should be same.",parent=self.forget_pass)
        else:
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            
            try:
                cur.execute("Update employee SET Pass=? where Empid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated successfully",parent=self.forget_pass)
                self.forget_pass.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
root=Tk()
obj=Login(root)
root.mainloop()

#get this function added once the billing dash is ready        
    #def logout(self):
    #    self.root.destroy()
    #    os.system("python login.py")