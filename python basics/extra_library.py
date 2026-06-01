# Extra library

import tkinter as tk                     # GUI making library(interactive interface)
from tkinter import *                    # To access all functions of tkinter [ (*) -> is used ]

#_____________________________________________________
# Tkinter library operations:
#_____________________________________________________

'''
win = tk.Tk()
win.title("First gui")
win.geometry()

label= tk.Label(win,text="click")
label.pack()

bt = tk.Button(win, text="click",command=lambda:print('hello world'))

bt.pack()

entry = tk.Entry(win)
entry.pack()
l1=0
def clicked():
    l1.configure(text="clicked")
    bt.Button(win,text="enter",command=clicked)

win.mainloop()

win=tk.Tk()
Menu_bar = tk.Menu(win)
file_menu = tk.Menu(Menu_bar,tearoff=0)
file_menu.add_command(label="open",command=open)
file_menu.add_command(label="Save",command=S)
file_menu.add_separator()
file_menu.add_command(label="exit",command=win.quit)
Menu_bar.add_cascade(label="file",menu=file_menu)
win.config(menu=Menu_bar)

win.mainloop()

#Simple Calculator

def add():
    result.set(float(entry1.get())+float(entry2.get()))

def subtract():
    result.set(float(entry1.get())-float(entry2.get()))

def multiply():
    result.set(float(entry1.get())*float(entry2.get()))

def divide():
    result.set(float(entry1.get())/float(entry2.get()))

root = tk.Tk()
root.title("Simple calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

result = tk.DoubleVar(root)
result_label = tk.Label(root,textvariable=result)
result_label.pack()

add_button = tk.Button(root,text="Add",command=add)
add_button.pack()

subtract_button = tk.Button(root,text="Sub",command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root,text="Multiply",command=multiply)
multiply_button.pack()

divide_button = tk.Button(root,text="Divide",command=divide)
divide_button.pack()

root.mainloop()

'''

