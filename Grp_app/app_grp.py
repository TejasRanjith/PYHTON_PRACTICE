# ALWAYS RUN FUNC_GRP.PY first to get the expected program
# Base for storing information
import tkinter as tk 
from tkinter import messagebox 

database = {}
data = {}


def chck_dict(e,p):
    from func_grp import main_datadict
    email_get = e.get()
    pass_get = p.get()
    for k in main_datadict:
        if k == email_get:
            if main_datadict[k][1] == pass_get:
                strdict = str(main_datadict[k])
    print(strdict)


def main_dict(f,l,e,p):
    firstname_get = f.get()
    email_get = e.get()
    lastname_get = l.get()
    pass_get = p.get()

    data[email_get] = [firstname_get+" "+lastname_get,pass_get]
    print(data)
    
    return data 


def space(r,c):
    return tk.Label(text = " ").grid(row = r,column = c)


def e_get():
    act_get = e_act.get()
    if act_get.lower() == "login":
        login = tk.Toplevel()
        login.title("LOGIN WINDOW")
        
        l_email = tk.Label(login,text = "E-mail :",font = "Arial 16 italic")
        l_pass = tk.Label(login,text = "Password :",font = "Arial 16 italic")

        e_email = tk.Entry(login)
        e_pass = tk.Entry(login,show = "*")

        

        func = lambda: chck_dict(e_email,e_pass)
        
        b_login = tk.Button(login,text = "Login",command = func)

        l_email.grid(row = 2,column = 0)
        e_email.grid(row = 2,column = 1)
        space(3,0)
        space(3,1)
        l_pass.grid(row = 4,column = 0)
        e_pass.grid(row = 4,column = 1)
        space(5,0)
        space(5,1)
        b_login.grid(row = 6,column = 0)
    
    elif act_get.lower() == "create":

        create = tk.Toplevel()
        create.title("CREATING ACCOUNT WINDOW")

        l_firstname = tk.Label(create,text = "First Name: ",font = "Arial 16 italic")
        l_lastname = tk.Label(create,text = "Last Name: ",font = "Arial 16 italic")
        l_pass = tk.Label(create,text = "Password :",font = "Arial 16 italic")
        l_email = tk.Label(create,text = "Email ID :",font = "Arial 16 italic")

        e_firstname = tk.Entry(create)
        e_lastname = tk.Entry(create)
        e_email = tk.Entry(create)
        e_pass = tk.Entry(create,show = "*")


        l_firstname.grid(row = 2,column = 0)
        e_firstname.grid(row = 2,column = 1)
        space(3,0)
        space(3,1)
        l_lastname.grid(row = 4,column = 0)
        e_lastname.grid(row = 4,column = 1)
        space(5,0)
        space(5,1)
        l_email.grid(row = 6,column = 0)
        e_email.grid(row = 6,column = 1)
        space(7,0)
        space(7,1)
        l_pass.grid(row = 8,column = 0)
        e_pass.grid(row = 8,column = 1)

        func = lambda: main_dict(e_firstname,e_lastname,e_email,e_pass)

        b_create = tk.Button(create,command = func,text = "Create Account")
        b_create.grid(row = 9,column= 0)

        

    elif act_get == "clear":
        pass
    else:
        pass
    

main = tk.Tk()
main.title("MAZE  BANK")
main.geometry("600x700")

l_act = tk.Label(font = "Times 16 italic bold",text = "Action : ")
e_act = tk.Entry(main)
b_act = tk.Button(main,text = "Action",command = e_get)
heading = tk.Label(text = "BANK MANAGER",font = "Times 50 bold underline")

heading.grid(columnspan = 50,row = 0,column = 0)
l_act.grid(row = 1,column = 0)
e_act.grid(row = 1,column = 1)
b_act.grid(row = 1,column = 2)



main.mainloop()
database.update(data)
#print(database)