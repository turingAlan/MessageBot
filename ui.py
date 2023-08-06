from tkinter import * 
from tkinter import ttk

root = Tk()
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# set the window size to half the screen size
root.geometry(str(screen_width//2)+"x"+str(screen_height//2))
root.title("InstaBot")

# page heading
title_label = ttk.Label(master=root,text= "InstaBot", font="Courier 24 bold")
title_label.pack()


# inputs
form_frame = ttk.Frame(master = root)
entry_username = StringVar()
entry_password = StringVar()
entry_target = StringVar()

# username
username_frame = ttk.Frame(master=form_frame)

username_label = ttk.Label(username_frame, text="Username: ")
username_label.pack(side = "left")
username_entry = ttk.Entry(master=username_frame,width = 50, textvariable=entry_username)
username_entry.pack(padx=20)

username_frame.pack(pady=20)

# password
passoword_frame = ttk.Frame(master=form_frame)

password_label = ttk.Label(master=passoword_frame, text="Password: ")
password_label.pack(side = "left")
password_entry = ttk.Entry(master=passoword_frame, width=50,textvariable=entry_password)
password_entry.pack(padx=20)

passoword_frame.pack(pady=20)

# target 
target_frame = ttk.Frame(master=form_frame)

target_label = ttk.Label(master=target_frame, text="Target: ")
target_label.pack(side = "left")
target_entry = ttk.Entry(master=target_frame, width=50,textvariable=entry_target)
target_entry.pack(padx=20)

target_frame.pack(pady=20)

# submit button
submit_button = ttk.Button(master=root, text="Submit")
submit_button.pack(side="bottom",pady=20)

form_frame.pack(pady=20)



root.mainloop()