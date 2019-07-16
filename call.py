from tkinter import *
from tkinter import messagebox
import os
def Insert1():
    import insert1
def Delete1():
    import delete1
def Update1():
    import update1
b=Tk()
b.title('Insert')
b.configure(background='RoyalBlue1')
b4=Button(b,text='Insert',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=Insert1)
b4.grid(row=6,column=0,padx=5,pady=10)
delb=Button(b,text='Delete',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=Delete1)
delb.grid(row=6,column=1,pady=10)
be=Button(b,text='Update',padx=20,pady=10,activebackground='purple3',activeforeground='black',command=Update1)
be.grid(row=5,column=2,pady=10)
b9=Button(b,text='Exit',padx=40,pady=10,activebackground='purple3',activeforeground='black',command=b.destroy)
b9.grid(row=6,column=2,padx=5,pady=10)
b.mainloop()
