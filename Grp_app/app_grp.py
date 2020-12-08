# Base for storing information
main_dict = {}
n = int(input("n --> "))
for i in range(1,n+1):
    grno = int(input("GR No. : "))
    name = input("Name --> ")
    cls = int(input("Class --> "))
    div = input("Divsion --> ")
    # and some other details......
    main_dict[grno] = [name,cls,div]
print(main_dict)
# Can be printed in the form of table using prettytable module....