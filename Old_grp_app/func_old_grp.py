def Name():
    name = input("YOUR NAME --> ")
    return name


def item():
    name = Name()
    items = input("AN ITEM --> ")
    f = open(f"LIST_{name.upper()}.txt","a+")
    f.write(items + "\n")
    f.close()
    f = open(f"LIST_{name.upper()}.txt","r")
    contents = f.read()
    print(contents)
    return items


def file_list():
    name = Name()
    items = input("AN ITEM -->")
    f = open(f"LIST_{name.upper()}.txt","a+")
    f.write(items + "\n")
    f.close()
    f = open(f"LIST_{name.upper()}.txt","r")
    contents = f.read()
    print(contents)


def file_list_read():
    name = Name()
    f = open(f"LIST_{name.upper()}.txt","r")
    contents = f.read()
    print(contents)


def file_clear():
    name = Name()
    f = open(f"LIST_{name.upper()}.txt","r")
    contents = f.read()
    f.close()
    a = input(f"ARE YOU SURE YOU WANT TO CLEAR THESE ITEMS {contents}(Y/N)?")
    while 1 == 1:
        if a.lower() == "y":        
            f = open(f"LIST_{name.upper()}.txt","w")
            f.write("")
            f.close()
            break
        elif a.lower() == "n":
            print("DELETION CANCELLED......")
            break
        else:
            print("I DIDN'T GET THAT!? ")
        

def file_del():
    name = Name()
    f = open(f"LIST_{name.upper()}.txt","r")
    contents = f.read()
    f.close()
    contents = contents.split(sep = "\n")
    while 1 == 1:
        try:
            obj = input("ITEM TO BE DELETED --> ")
            i = contents.index(obj)
            contents[i] = ""
            break
        except ValueError:
            print("ITEM NOT FOUND !!")
    f = open(f"LIST_{name.upper()}.txt","w")
    for l in contents:
        f.write(l + "\n")
    f.close()