import random,os

l = ["I","C","C","C"]
random.shuffle(l)
for elem in l:
    input("")
    print(elem)
    input("")
    os.system("cls")
input("")
print(l)
# from pynput.mouse import Button, Controller
# def timer(n):
#     import time
#     time.sleep(n)

# mouse = Controller()

# while True:
#     print(mouse.position)
#     timer(1)