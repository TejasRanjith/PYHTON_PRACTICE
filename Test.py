import functions
a = input("o - add data to the file (TEST.txt) | r - open a file | 0 - exit the program --> ")
while a != "0":
    
    if a.lower() == "o":
        functions.file_opening()
        a = input("o - add data to the file (TEST.txt) | r - open a file  --> ")
    elif a.lower() == "r":
        functions.file_reader()
        a = input("o - add data to the file (TEST.txt) | r - open a file  --> ")
    elif a.lower() == "0":
        break
    else:
        pass
