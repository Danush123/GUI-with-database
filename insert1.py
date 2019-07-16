from tkinter import *
from tkinter import messagebox
import os
import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/oracle@localhost')
cur=conn.cursor()

def Insert1():
    try:
        pid=p_ide.get()
        pname=p_namee.get()
        stock=stocke.get()
        price=pricee.get()
        description=descriptione.get()
        rating=ratinge.get()
        new=[(pid,pname,stock,price,description,rating)]
        cur.executemany("insert into project(p_id,p_name,stock,price,description,rating) values (:1,:2,:3,:4,:5,:6)",new)
        conn.commit()
        Display2()
    except:
        messagebox.showerror("Error","Insert unsuccessful!")

def Display2():
    messagebox.showinfo("Notification","Successfully Inserted")

b=Tk()
b.title('Insert')
b.configure(background='RoyalBlue1')
p_idl=Label(b,text='Product ID',bg='RoyalBlue1')
p_idl.grid(row=0,column=0,padx=20,pady=10)
p_ide=Entry(b)
p_ide.grid(row=0,column=1)
p_namel=Label(b,text='Product Name',bg='RoyalBlue1')
p_namel.grid(row=1,column=0,padx=0,pady=10)
p_namee=Entry(b)
p_namee.grid(row=1,column=1)
stockl=Label(b,text='Stock',bg='RoyalBlue1')
stockl.grid(row=2,column=0,padx=40,pady=10)
stocke=Entry(b)
stocke.grid(row=2,column=1)
pricel=Label(b,text='Price',bg='RoyalBlue1')
pricel.grid(row=3,column=0,padx=40,pady=10)
pricee=Entry(b)
pricee.grid(row=3,column=1)
descriptionl=Label(b,text='Description',bg='RoyalBlue1')
descriptionl.grid(row=4,column=0,padx=40,pady=10)
descriptione=Entry(b)
descriptione.grid(row=4,column=1)
ratingl=Label(b,text='Rating',bg='RoyalBlue1')
ratingl.grid(row=5,column=0,padx=40,pady=10)
ratinge=Entry(b)
ratinge.grid(row=5,column=1)
b4=Button(b,text='Insert',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=Insert1)
b4.grid(row=6,column=0,padx=5,pady=10)
b9=Button(b,text='Exit',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=b.destroy)
b9.grid(row=6,column=2,padx=5,pady=10)
b.mainloop()
