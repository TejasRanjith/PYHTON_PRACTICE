#part 3. :
import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
e = tk.Entry(root)
e.grid(row=0,column = 1)
#(0,"Enter your name")..... here 0 means the index
e.insert(0,"Enter Your Name : ")
def myclick():
    mylabel = tk.Label(root, text = "Hello "+e.get())
    mylabel.grid(row = 2,column = 1)


def space(r,c):
    return tk.Label(text = " ").grid(row = r,column = c)

space(0,0)
mybutton = tk.Button(root,text="Enter your name",padx = 50,pady = 50,command = myclick,fg = "white",bg = "black")
mybutton.grid(row = 1,column = 1)

root.mainloop()
