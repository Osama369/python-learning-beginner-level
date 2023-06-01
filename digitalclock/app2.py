# we are going to  make digital clock in python
# models used in projects  
#1 tkinter
#2 Datetime 

# from _tkinter import *
# from cProfile import label
from tkinter import *
from tkinter.ttk import *
from time import strftime

clock= Tk()
clock.title("Digital Clock")
def time():
    string= strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label= Label(clock,font=("ds-digital",80), background="black", foreground="white")
label.pack(anchor="center")
time()

clock.mainloop()



