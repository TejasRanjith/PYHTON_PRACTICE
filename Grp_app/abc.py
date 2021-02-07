main_database = open("main_database.txt","r")
contents = main_database.read()
main_database.close()

#contents = list(dict.fromkeys(contents))
main_dict = []

for elem in contents.split(sep = "\n"):
    print(elem)
    if elem not in main_dict:
        main_dict.append(elem)
print(main_dict)
["{'tejas': ['050', 'T', 'R', '00', '050', 100]}", '{}', '', "{' ': [' ', ' ', ' ', ' ']}"]