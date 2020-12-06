#part 3. :
import tkinter as tk

root = tk.Tk()

e = tk.Entry(root,width = 50,bg = "black",fg = "white",borderwidth = 10)
e.pack()#(0,"Enetryour name")..... here 0 means the index
e.insert(0,"Enter Your Name : ")
def myclick():
    mylabel = tk.Label(root, text = "Hello "+e.get())
    mylabel.pack()



mybutton = tk.Button(root,text="Enter your name",padx = 50,pady = 50,command = myclick,fg = "white",bg = "black")
mybutton.pack()

root.mainloop()
