import func_grp
while 1 == 1:
    print("Insert Following Shortcuts for performing functions:")
    print("O == For opening or creating a list and then displays the edited list.")
    print("A == For adding items to the LIST FILE.")
    print("C == For clearing items after confirmation.")
    print("R == For reading your list")
    print("0 == To exit the program")
    print("D == To delete a particular element")
    a = input("--> ")
    if a.lower() == "o" :
        func_grp.file_list()

    elif a.lower() == "a":
        func_grp.item()

    elif a.lower() == "c":
        func_grp.file_clear()

    elif a.lower() == "r":
        func_grp.file_list_read()
        
    elif a.lower() == "0":
        print("THANK YOU FOR USING SHOPPING LIST EDITOR V1.0 :) ")
        break

    elif a.lower() == "d":
        func_grp.file_del()
    else:
        print("I DIDN'T GET THAT!?")


input("PRESS ENTER TO COMPLETELY TERMINATE THE PROGRAM :)  ")


