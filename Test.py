import functions
import webbrowser
a = input("o - add data to the file (TEST.txt) | r - open a file | 0 - exit the program | c - clear the data --> ")
while a != "0":
    if a.lower() == "o":
        functions.file_opening()
        a = input("o - add data to the file (TEST.txt) | r - open a file | 0 - exit the program | c - clear the data --> ")
    elif a.lower() == "r":
        result = functions.file_reader()
        a = input("o - add data to the file (TEST.txt) | r - open a file | 0 - exit the program | c - clear the data --> ")
    elif a.lower() == "c":
        functions.file_clear()
        a = input("o - add data to the file (TEST.txt) | r - open a file | 0 - exit the program | c - clear the data --> ")
    elif a.lower() == "0":
        break
    else:
        break
r = input("Do you want to open the websites provided in the file ? (Y/N)")
if r.lower() == "y":
    try:
        for url in result.split(sep = "\n"):
            webbrowser.open_new(url)
    except NameError:
        print()
    print("Thank You for using the program")
elif r.lower() == "n":
    print("Thank You for using the program")