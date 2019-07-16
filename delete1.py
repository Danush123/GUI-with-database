from tkinter import *
from tkinter import messagebox
import os
import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/oracle@localhost')
cur=conn.cursor()

def Delete1():
    try:
        pid=p_ide.get()
        new=[pid]
        cur.execute("delete from project where p_id=:1",new)
        conn.commit()
        Display1()
    except:
        messagebox.showerror("Error","Delete unsuccessful!")
def Display1():
    messagebox.showinfo("Notification","Successfully Deleted")
    b.destroy()

b=Tk()
b.title('Insert')
b.configure(background='RoyalBlue1')
p_idl=Label(b,text='Product ID',bg='RoyalBlue1')
p_idl.grid(row=0,column=0,padx=20,pady=10)
p_ide=Entry(b)
p_ide.grid(row=0,column=1)
delb=Button(b,text='Delete',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=Delete1)
delb.grid(row=6,column=1,pady=10)
b9=Button(b,text='Exit',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=b.destroy)
b9.grid(row=6,column=2,padx=5,pady=10)
b.mainloop()
