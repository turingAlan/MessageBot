from tkinter import * 
from tkinter import ttk

root = Tk()
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# set the window size to half the screen size
root.geometry(str(screen_width//2)+"x"+str(screen_height//2))
root.title("InstaBot")

title_label = ttk.Label(master=root,text= "InstaBot", font="Courier 30 bold")
title_label.pack()


# root.grid()
test = ttk.Label(root,text = "Message")
test.pack(side="left")
exit = ttk.Button(root,text="quit",command = quit)
exit.pack(side="right")


root.mainloop()