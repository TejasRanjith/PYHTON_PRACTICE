# Made by Tejas and Nihad....
#  Main features
# 1.) stores accounts in a file so that it can be used again (database)
# 2.) has secret commands.
from app_grp import main_datadict

main_database = open("main_database.txt","a+")
for i in range(0,1):
    main_database.write(str(main_datadict)+"\n")
    main_database.write("{}"+"\n")
    main_database.write(''+"\n")
    main_database.write("{'@.com': [' ', ' ', ' ', ' ', ' ', 100]}"+"\n")
main_database.close()

main_database = open("main_database.txt","r")
contents = main_database.read()
main_database.close()
new_contents = []
for elem in contents.split(sep = "\n"):
    if elem not in new_contents:
        new_contents.append(elem)
new_contents.remove("{}")
new_contents.remove('')
new_contents.remove("{'@.com': [' ', ' ', ' ', ' ', ' ', 100]}")

for i in range(0,len(new_contents)):
    main_datadict.update(eval(new_contents[i]))