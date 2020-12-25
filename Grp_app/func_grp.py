from app_grp import database

main_datadict = {}
main_database = open("main_database.txt","a+")
for i in range(0,1):
    main_database.write(str(database)+"\n")
main_database.close()

main_database = open("main_database.txt","r")
contents = main_database.read()
main_database.close()

contents = list(set(contents.split(sep = "\n")))
contents.remove("{}")
contents.remove('')
#contents.remove("{'': [' ', '']}")


#for i in range(0,len(contents)):
#    main_datadict.update(eval(contents[i]))
#print(main_datadict)
