import pickle as pkl

def writefile(s=list()):
    with open("Employees.dat","wb") as f:
        pkl.dump(s, f)
    
def readfile():
    with open("Employees.dat","rb") as f:
        cont = pkl.load(f)
        return cont

def emp_info():
    emp = input("Employee No. -->")
    name = input("Name --> ")
    desgn = input("Designation --> ")
    sal = int(input("Salary --> "))
    emp_list = [emp,name,desgn,sal]
    return emp_list

def add_emp():
    l = readfile()
    l.append(emp_info())
    writefile(l)

def update():
    d = readfile()
    print(d)

# update()

#! Menu
while True:
    print("\tMenu\n")
    print(5*"\tINFO\n")
    opt = input("[c,r,a,0]--> ");opt = opt.lower()
    if opt == "c":
        writefile()
    elif opt == "r":
        print(readfile())
    elif opt == "a":
        add_emp()
    elif opt == "u":
        update()
    elif opt == "0":
        break
    else:
        print("Invalid Option....")


#?------------------------------------------------------------------------------------------------------------------------------
def timer(n=0):
    import time
    time.sleep(n)

# def writefile(s=dict()):
#     with open("Students.dat","wb") as f:
#         pkl.dump(s,f)

# def readfile():
#     with open("Students.dat","rb") as f:
#         cont = pkl.load(f)
#         return cont

def add_std():
    c,d = readfile(),std_info()
    c.update(d)
    writefile(c)

def std_info():
    n,std_dict = int(input("\nNumber of Students: ")),dict()
    for i in range(1,n+1):
        print(f"\nDetails of the student {i}:")
        name,roll,marks = input("\nName --> "),int(input("Roll No. --> ")),int(input("Marks --> "))
        std_dict[roll] = [name,marks]
    return std_dict
#!  <<<<--  __MAIN__  -->>>>
while True:
    print("<<---- MENU  ---->>")
    print("",
    "To create a file if you dont have --> c",
    "To add n number of students to the file --> a",
    "To see all the contents in the file --> r",
    "To stop the main program --> 0",
    "",sep="\n")
    opt = input("\nYour Option --> ")
    opt = opt.lower()
    if opt == "c":
        print("\nCreating the file....")
        timer(0.8)
        writefile()
        print("\nFile Created.")
    elif opt == "a":
        print("\nTaking you to 'student info' program...\n")
        timer(0.5)
        add_std()
        print("\nInformation/Informations added")
    elif opt == "r":
        print("\nEntire Student information displayed below:\n")
        d = readfile()
        for elem in d:
            print(f"Roll No.: {elem}",
            f"Name: {d[elem][0]}",
            f"Marks: {d[elem][1]}",
            "",
            sep="\n")
    elif opt == "0":
        timer(1)
        print("\n"+"Thank you for using the string modifier program."+"\n")
        timer(1)
        print("Hope to see you soon in string modifier program version 1.2.0"+"\n"+"\n")
        timer(1.5)
        print("Program exited with exit code 0"+"\n")
        break
    else:
        pass