from cProfile import label
from cgitb import text
from distutils.cmd import Command
from distutils.command.config import config
from re import X
import tkinter as tk
from tkinter import ttk
from webbrowser import get

def ConvertValues():
    cfsv=0
    fsv=inputV1.get('1.0','end')
    if(combobox.get()=='rem' and comboboxC.get()=='px' or combobox.get()=='em' and comboboxC.get()=='px'):
        cfsv=float(fsv)*16
        label3.config(text="The converted value is:" + " "+str(cfsv))
    if(combobox.get()=='rem' and comboboxC.get()=='em' or combobox.get()=='em' and comboboxC.get()=='rem' ):
        label3.config(text="The converted value is:" + " "+str(float(fsv)))
    if(combobox.get()=='rem' and comboboxC.get()=='rem' or combobox.get()=='rem' and comboboxC.get()=='rem' ):
        label3.config(text="The converted value is:" + " "+str(float(fsv)))
    if(combobox.get()=='px' and comboboxC.get()=='rem' or combobox.get()=='px' and comboboxC.get()=='em'):
        cfsv=float(fsv)*0.0625
        label3.config(text="The converted value is:" + " "+str(cfsv))

root = tk.Tk()
global current_var
global convert_var
global label1
global label2
global label3
global inputV1
global combobox
global comboboxC
global btn
root.title('FontSizeConvert')
root.geometry('600x400+50+50')
root.resizable(False, False)
root.iconbitmap('./src/logo.ico')
root.configure(background='#D5F5E3')
# Create Label 
label1=tk.Label(root, text="Type the value for the font size")
label1.place(x=10, y=50)
# Create Text for fontsize value 1 
inputV1=tk.Text(root,height=1, width=10)
inputV1.place(x=185,y=50)
# Create Combobox for font sizing 
current_var = tk.StringVar()
combobox = ttk.Combobox(root,textvariable=current_var)
combobox['values']=('em','rem','px')
combobox.place(x=280,y=50)
combobox.current(1)
# Create label for information
label2=tk.Label(root, text="Select the value to convert to")
label2.place(x=10,y=90)
# Create Combobox for convert font size 
convert_var = tk.StringVar()
comboboxC = ttk.Combobox(root,textvariable=convert_var)
comboboxC['values']=('em','rem','px')
comboboxC.place(x=180,y=90)
comboboxC.current(1)
# Create button for convert font size values
btn=tk.Button(root,text='CONVERT', command=ConvertValues)
btn.place(x=330,y=88)
# Create label for convert size 
label3=tk.Label(root,text="The converted value is:")
label3.place(x=10,y=130)

root.mainloop()

