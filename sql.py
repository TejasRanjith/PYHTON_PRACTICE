def connection(db):
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="Tejas@035611",database=db)
    return mydb

def show_dbs(db):
    import prettytable,time
#.r creating connection
    mydb = connection(db=db)
    myc = mydb.cursor()
#.y creating cursor to execute statement
    t1 = time.time()
    myc.execute("show databases;")
#.g creating prettytable instance
    t = prettytable.PrettyTable()
    i,t.field_names = 0,["Databases"]
#.b adding rows to the table
    for x in myc:
        t.add_row(x)
        i+=1
#.r printing the terminal output with time
    t2 = time.time()
    duration = round(t2-t1,2)
    print("",t,sep="\n")
    print("\n"+f"{i} rows in set ({duration} sec)\n")

show_dbs("school")

def disp_table(table,db):
    import prettytable,time
#.y creating connection
    mydb = connection(db=db)
    myc = mydb.cursor()
#.g getting column names
    t1 = time.time()
    myc.execute(f"desc {table}")
    t,l = prettytable.PrettyTable(),[]
    for x in myc:
        l.append(x[0])
    t.field_names,i = l,0
#.b adding rows to the table
    myc.execute(f"select * from {table}")
    for x in myc:
        t.add_row(x)
        i+=1
#.r printing the table
    print(t)
#.y printing the terminal output with time
    t2 = time.time()
    duration = round(t2-t1,2)
    print("\n"+f"{i} rows in set ({duration} sec)\n")

disp_table("products","store")

def query():
    pass
