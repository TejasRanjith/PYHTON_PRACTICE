main_datadict = {}
def restart():
    import os     #Bank_Management_System.py
    os.system("python grp_app//Bank_Management_System.py")


def sys_log():
    from Bank_Management_System import new_contents
    for elem in new_contents:
        print(elem)


def login():
    while 1==1:
        print()
        print("Type 'B' to check balance.")
        print("Type 'W' to withdraw amount.")
        print("Type 'D' to deposit particular amount.")
        print("Type 'DEL' to delete the account")
        print("Type 'L' to logout from your account.")
        print()
        b = input("Action --> ")
        b = b.lower()
        if b == "b":
            print()
            print("Balance of the account,",email_id,"is :",main_datadict[k][5],"AED")
        elif b == "del":
            print()
            print("**  ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT FOREVER ? (Y/N)  **")
            print("REMAINING BALANCE :",main_datadict[k][5])
            opt = input("--> ")
            if opt.lower() == "y":
                print("YOUR ACOUNT",k,"HAS BEEN DELETED")
                del main_datadict[k]
                break
            else:
                print("DELETION CANCELLED.......")
        elif b == "w":
            print()
            w = int(input("Amount to be withdrawed : "))
            if w > 0:
                if w < main_datadict[k][5]:
                    main_datadict[k][5] = main_datadict[k][5] - w
                    print("Remaining Balance after withdrawal,",main_datadict[k][5],"AED")
                else:
                    print("Sorry you don't have enough balance to withdraw : Please Deposit some amount")
            else:
                print("*** INVALID AMOUNT ***")
        elif b == "d":
            print()
            d = int(input("Amount to be deposited : "))
            if d > 0:
                main_datadict[k][5] = main_datadict[k][5] + d
                print("New Balance after deposition,",main_datadict[k][5],"AED")
            else:
                print("*** INVALID AMOUNT ***")
        elif b == "l":
            print()
            print("YOU HAVE BEEN LOGGED OUT")
            break
        else:
            print("INVALID OPTION")



print()
print("         *** BANK MANAGEMENT SYSTEM ***")
while 1 == 1:
    print()
    print("=<<  Type 'L' to login if you have an acount.    >>=")
    print("=<<  Type 'C' to create an account.              >>=")
    print("=<<  Type '0' to exit the program.               >>=")
    print()
    a = input("Action --> ")
    a = a.lower()
# a is received in lower alphabet. 
    if a == "l":
        from Bank_Management_System import main_datadict
        print()
        email_id = input("REGISTERED EMAIL ID : ")
        while 1 == 1:
            if "@" and ".com" in email_id:
                break
            else:
                print("PLEASE ENTER A VALID EMAIL ID..")
                email_id = input("REGISTERED EMAIL ID : ")
        password = input("PASSWORD : ")
        for k in main_datadict:
            if k == email_id:
                if password == main_datadict[k][0]:
                    print()
                    print("Name:",main_datadict[k][1],main_datadict[k][2],)
                    print("Date of Birth:",main_datadict[k][3])
                    print("Phone number:",main_datadict[k][4])
                    login()
                    new_main_datadict = {}
                    new_main_datadict.update(main_datadict)
                    main_database = open("main_database.txt","w")
                    main_database.write(str(main_datadict)+"\n")
                    main_database.close()
                else:
                    print("WRONG PASSWORD. PLEASE TRY AGAIN....")
            else:
                print("EMAIL ID NOT FOUND. PLEASE RESGISTER")
    elif a == "log":
        sys_log()

    elif a == "c":
        print()
        print("RESGISTRATION FORM")
        print()
        firstname = input("FIRST NAME : ")
        lastname = input("LAST NAME : ")
        dob = input("DATE OF BIRTH (DD/MM/YYYY) : ")
        phoneno = input("PHONE NO. : ")
        email_id = input("EMAIL ID : ")
        while 1==1:
            if "@" and ".com" in email_id:
                break
            else:
                print("PLEASE ENTER A VALID EMAIL ID.")
                email_id = input("EMAIL ID : ")
        newpass = input("NEW PASSWORD : ")
        print()
        print("Minimum Requirements : Add Balance (100 AED)")
        balance = int(input("FIRST DEPOSIT: "))
        if balance < 100:
            print("MINIMUM AMOUNT == 100 AED ")
            balance = int(input("FIRST DEPOSIT: "))
        else:
            print("YOUR ACCOUNT HAS BEEN CREATED....")
            new_main_datadict = {}
            new_main_datadict.update(main_datadict)
            main_database = open("main_database.txt","w")
            main_database.write(str(main_datadict)+"\n")
            main_database.close()
        
        for i in range(0,1):      # 0  ,  1  ,  2  ,  3  ,  4   ,   5
            main_datadict[email_id] = [newpass,firstname,lastname,dob,phoneno,balance]     
        
    elif a == "0":
        print()
        print('''THANK YOU FOR USING THE PROGRAM 
        WE EXPECT YOU TO COME BACK AGAIN :)  
(press enter to completely terminate the program)''')
        a = input()
        if a.lower() == "restart":
            restart()
            break
        else:
            break