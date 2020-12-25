import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("MSGBOX!!!")

def popup():
    response = messagebox.askokcancel("Information","Hi this is a message box.......")
    tk.Label(root,text = response).pack()
# messagebox. (showinfo,showerror,showwarning,askquestion,askokcancel,askyesno)


b = tk.Button(text = "POPUP",command = popup)

b.pack()

root.mainloop()