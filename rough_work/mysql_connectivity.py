import mysql.connector as ms
import prettytable as pt

mydb = ms.connect(user = "root",host = "localhost",
password = "Tejas@035611",database = "revision")
myc = mydb.cursor()

# myc.execute("create table products(PID int primary key, Pname varchar(20), Price int)")

# myc.execute("""insert into products values(101,'Digital Camera 14X',12000),
#                 (102,'Digital Pad 11i',22000),(104,'Pen Drive 16 GB',1100),
#                 (105,'Car GPS System',12000),(106,'Led Screen 32',28000);""")
# mydb.commit()

def add():
    pid = int(input("Enter Product ID: "))
    pname = input("Enter Product Name: ")
    price = int(input("Enter Product Price: "))
    myc.execute(f"insert into products value({pid},'{pname}',{price});")
    mydb.commit()
    print("Product Added Successfully")

def update():
    pid = int(input("Enter PID of Product to be updated: "))
    pname = input("Enter New Product Name: ")
    price = int(input("Enter New Product Price: "))
    myc.execute(f"update products set Pname='{pname}',Price={price} where PID={pid};")
    mydb.commit()
    print("Product Updated Successfully")

def delete():
    pid = int(input("Enter PID of Product to be deleted: "))
    myc.execute(f"delete from products where PID={pid};")
    mydb.commit()
    print("Product Deleted Successfully")

def display():
    myc.execute("select * from products;")
    result = myc.fetchall()
    print(result)
    t = pt.PrettyTable()
    t.field_names = ["PID","Pname","Price"]
    for i in result:
        t.add_row(i)
    print(t)

#.r Main

def timer(n):
    import time
    time.sleep(n)

def opt_0():
    timer(1)
    print('\n'+'Thank you for using the program.'+'\n')
    timer(1)
    print('Hope to see you soon in program version 1.2.0'+'\n'+'\n')
    timer(1.5)
    print('Program exited with exit code 0'+'\n')
    exit()

l_opt = ['a','u','del','d','0']
l_func = ['add()','update()','delete()','display()','opt_0()']
d_menu = {
    'a':  'To add a product         ',
    'u':  'To update a product      ',
    'del':'To delete a product      ',
    'd':  'To display all products  ',
    '0':  'To stop the main program '
}

while True:
    print('\n<<----  MENU  ---->>\n')
    for elem in d_menu:
        print('  '+d_menu[elem] + '  --> ' + elem)
    opt = input('\nYour Option -->').lower()
    print()
    if opt in l_opt:
        for elem in l_opt:
            if opt == elem:
                eval(l_func[l_opt.index(elem)])
    elif opt == '0':
        opt_0()
        break
    else:
        print('Invalid Option......')