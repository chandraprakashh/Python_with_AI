# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:48:09 2019

@author: Administrator
"""

import tkinter as tk
import tkinter.messagebox as msg 

ram = tk.Tk()

def chandu():
    msg.showinfo("Message" , "welcome my page")
    
c = tk.Button(ram , text="click" , command = chandu)
c.pack()

ram.mainloop()
