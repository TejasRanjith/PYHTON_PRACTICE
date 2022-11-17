Herbs={'Adrak':'Ginger', 'Amla': 'Gooseberry', 
'Babool': 'Indian Gum', 'Dhania': 'Coriander', 
'Lahsun':'Garlic', 'Tulsi': 'Basil'}
s = []
def push(stack,obj):
    stack.append(obj)

def pop(stack):
    if len(stack) == 0:
        return "Stack is empty"
    else:
        return f"{stack.pop()}".removeprefix("(").removesuffix(")")

def push_item():
    for elem in Herbs.items():
        if elem[1][0] == 'G':
            push(s,elem)

def pop_display():
    while len(s) != 0:
        print(pop(s))

push_item()
pop_display()

# n = [1,2,3,4,5,6,7,8,9,10]
# a = [1,2,3,4,5,6,7,8,9,10,11]
# if (n:=len(a)) == 10:
#     print(True)