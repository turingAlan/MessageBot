from tkinter import * 
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root,padding  = 30)
root.title("My first python GUI")
frm.grid()
ttk.Label(frm,text = "Message").grid(column = 0,row = 0)
ttk.Button(frm,text="quit",command = quit).grid(column = 0,row = 1)

root.mainloop()