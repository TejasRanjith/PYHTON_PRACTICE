from random import randint
nums = nums=[randint(10,99) for I in range(7)]
s = []

def push(stack,obj):
    stack.append(obj)

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack.pop(),end=" ")

def display(stack):
    for elem in stack[::-1]:
        print(elem,end=" ")

def user_push():
    for num in nums:
        if num % 2 == 0:
            push(s,num)
    for num in nums:
        if num % 2 != 0:
            push(s,num)

def user_pop():
    while len(s) > 0:
        pop(s)

user_push()
# print(s)
# display(s)
user_pop()