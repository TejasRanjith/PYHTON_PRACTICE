import tkinter as tk

root = tk.Tk()

def myclick():
    mylabel = tk.Label(root, text = "ADDED A STUDENT")
    mylabel.pack()


mybutton = tk.Button(root,text="TO ADD A STUDENT",padx = 50,pady = 50,command = myclick,fg = "BLUE",bg = "#ffffff")
mybutton.pack()

root.mainloop()
