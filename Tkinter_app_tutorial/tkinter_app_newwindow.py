import tkinter as tk
 
root = tk.Tk()
root.title("Making Different Windows......")


window1 = tk.Toplevel()
window1.title("NEW WINDOW")
tk.Label(window1,text = " HELLO WORLD !").pack()






tk.mainloop()