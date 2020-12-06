#part 1. :
import tkinter

root = tkinter.Tk()

# Creating Label
mylabel1 = tkinter.Label(root,text = "HELLO WORLD!!!")
mylabel2 = tkinter.Label(root,text = "MY NAME IS TEJAS RANJITH.")

# Showing it onto screen 
mylabel1.grid(row = 0,column = 0)
mylabel2.grid(row = 1,column = 1)

root.mainloop()
