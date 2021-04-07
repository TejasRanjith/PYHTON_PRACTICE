import webbrowser
import time

# def timer(n):
#     import time
#     time.sleep(n)

while 1==1:
    print()
    print("<<<<----  INTERACTIVE WEBSITE OPENER  ---->>>>")
    print("Please go through the folowing options:")
    print("To add a website : add")
    print("To display the list of websites : list")
    print("To open the websites in the given list : open")
    print("To stop the program : stop")
    print()
    opt = input("OPTION --> ")
    print()
    if opt == "add":
        n = int(input("Number of websites to be added : "))
        for i in range(n):
            website = input("The website address : ")
            f = open("websites.txt","a+")
            f.write(website+"\n")
            f.close()
    elif opt == "list":
        f = open("websites.txt","r+")
        contents = f.read()
        f.close()
        if contents == "":
            print("Please add a website.")
        else:
            print(contents)
    elif opt == "open":
        f = open("websites.txt","r+")
        contents = f.read()
        f.close()
        l = contents.split(sep = "\n")
        for elem in l:
            webbrowser.open_new(elem)
    elif opt == "stop":
        print("Thank you for using the interactive program")
        print()
        print("                 -Made by Tejas Ranjith")
        print()
        break
    else:
        print("Invalid Option. Please try again.....")
print("[  press enter to exit the program :)  ]")
input()