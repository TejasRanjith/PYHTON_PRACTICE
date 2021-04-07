import tkinter as tk

main = tk.Tk("MY APP")
main.iconbitmap("C://Users//home//Desktop//Cornmanthe3rd-Plex-Other-python.ico") ####required.........
main.title("MY APP")


bg = tk.PhotoImage(file = "C://Users//home//Desktop//image.png")
li = tk.Label(main,image = bg)
l1 = tk.Label(main,text = "Heading",font = ("Times New Roman",32,"bold","italic"))
b1 = tk.Button(main,text = "CLICK ME!!!!")

# li.place(x = 0,y = 0,relwidth = 1,relheight = 1)
li.pack()
l1.pack()
b1.pack()






main.mainloop()