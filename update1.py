from tkinter import *
from tkinter import messagebox
import os
import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/oracle@localhost')
cur=conn.cursor()

def Update1():
    try:
        pid=p_ide.get()
        pname=p_namee.get()
        new=[pname,pid]
        cur.execute("update project set p_name=:1 where p_id=:2",new)
        conn.commit()
        Display()
    except:
        messagebox.showerror("Error","Update unsuccessful!")
def Update2():
    try:
        pid=p_ide.get()
        stock=stocke.get()
        new=[stock,pid]
        cur.execute("update project set stock=:1 where p_id=:2",new)
        if stock<'200':
            messagebox.showwarning("Warning","Low Stock, Please Restock!")
            Display()
        else:
            Display()
        conn.commit()
    except:
        messagebox.showerror("Error","Update unsuccessful!")
def Update3():
    try:
        pid=p_ide.get()
        price=pricee.get()
        new=[price,pid]
        cur.execute("update project set price=:1 where p_id=:2",new)
        conn.commit()
        Display()
    except:
        messagebox.showerror("Error","Update unsuccessful!")
def Update4():
    try:
        pid=p_ide.get()
        description=descriptione.get()
        new=[description,pid]
        cur.execute("update project set description=:1 where p_id=:2",new)
        conn.commit()
        Display()
    except:
        messagebox.showerror("Error","Update unsuccessful!")
def Update5():
    try:
        pid=p_ide.get()
        rating=ratinge.get()
        new=[rating,pid]
        cur.execute("update project set rating=:1 where p_id=:2",new)
        conn.commit()
        Display()
    except:
        messagebox.showerror("Error","Update unsuccessful!")
def Display():
    messagebox.showinfo("Notification","Successfully Updated")

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
ba=Button(b,text='Update',padx=20,pady=5,activebackground='purple3',activeforeground='black',command=Update1)
ba.grid(row=1,column=2,padx=15,pady=10)
stockl=Label(b,text='Stock',bg='RoyalBlue1')
stockl.grid(row=2,column=0,padx=40,pady=10)
stocke=Entry(b)
stocke.grid(row=2,column=1)
bb=Button(b,text='Update',padx=20,pady=10,activebackground='purple3',activeforeground='black',command=Update2)
bb.grid(row=2,column=2,pady=10)
pricel=Label(b,text='Price',bg='RoyalBlue1')
pricel.grid(row=3,column=0,padx=40,pady=10)
pricee=Entry(b)
pricee.grid(row=3,column=1)
bc=Button(b,text='Update',padx=20,pady=10,activebackground='purple3',activeforeground='black',command=Update3)
bc.grid(row=3,column=2,pady=10)
descriptionl=Label(b,text='Description',bg='RoyalBlue1')
descriptionl.grid(row=4,column=0,padx=40,pady=10)
descriptione=Entry(b)
descriptione.grid(row=4,column=1)
bd=Button(b,text='Update',padx=20,pady=10,activebackground='purple3',activeforeground='black',command=Update4)
bd.grid(row=4,column=2,pady=10)
ratingl=Label(b,text='Rating',bg='RoyalBlue1')
ratingl.grid(row=5,column=0,padx=40,pady=10)
ratinge=Entry(b)
ratinge.grid(row=5,column=1)
be=Button(b,text='Update',padx=20,pady=10,activebackground='purple3',activeforeground='black',command=Update5)
be.grid(row=5,column=2,pady=10)
b9=Button(b,text='Exit',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=b.destroy)
b9.grid(row=6,column=2,padx=5,pady=10)
b.mainloop()
