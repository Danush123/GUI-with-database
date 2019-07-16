import os
import sys
from tkinter import *
from tkinter import messagebox
def callfn():
    user=e1.get()
    passwd=e2.get()
    if(user=='danush' and passwd=='12345'):
        a.destroy()
        import call
    else:
        messagebox.showerror("Error","Invalid credentials!")
a=Tk()
a.title('Login')
a.configure(background='dark violet')
l1=Label(a,text='Username',bg='dark violet')
l1.grid(row=0,column=0)
l2=Label(a,text='Password',bg='dark violet')
l2.grid(row=1,column=0)
e1=Entry(a)
e1.grid(row=0,column=1,padx=15,pady=10)
e2=Entry(a,show='*')
e2.grid(row=1,column=1)
b=Button(a,text='login',bg='gray50',command=callfn)
b.grid(row=4,column=0,padx=20,pady=10)
a.mainloop()
