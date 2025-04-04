import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Empid INTEGER PRIMARY KEY AUTOINCREMENT , Name text, Email text, Gender text, Contact text, DOB text, DOJ text, Pass text, Utype text, Address text, Salary text)")
    con.commit()
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT , name text, contact text,desc text)")
    con.commit()
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT , Name text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT , Supplier text, Category text,  Name text, Price text, Quantity text, Status text)")
    con.commit()
    
create_db()