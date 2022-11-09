# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:39:18 2019

@author: 18pt16
"""

import pure as pr
import tkinter as tk

mainWin = tk.Tk()

def print_fact():
   p = E1.get()
   E1.delete(0,"end")
   if len(p)>0:
       x = pr.prime_fact(int(p))
       print(x)
   var2 = tk.StringVar()
   F3 = tk.Frame(mainWin)
   F3.pack(padx=10,pady=30,side = 'top')
   L2 = tk.Label(F3,text="Factors",textvariable = var2)
   var2.set(x)
   L2.pack()

mainWin.geometry("500x500")
mainWin.resizable(0,0)
mainWin.configure(bg = "red")

F2 = tk.Frame(mainWin)
F2.pack(padx=10,pady=20,side = 'top')

L1 = tk.Label(F2, text="Number")
var1 = tk.StringVar()

E1 = tk.Entry(F2, bd = 5,textvariable = var1)
L1.pack( side = 'left')
E1.pack(side = 'right')

F = tk.Frame(mainWin)
F.pack(padx=10,pady=30,side = 'top')
B = tk.Button(F ,text = "Create Group",command = print_fact)
B.pack()

mainWin.mainloop()
