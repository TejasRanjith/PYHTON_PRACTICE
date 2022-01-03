from pynput.mouse import Button,Controller
from pynput.keyboard import Key
mouse = Controller()

def key(*words):
    from pynput.keyboard import Key,Controller
    k = Controller()

    for word in words:
        if type(word) == str and len(word) != 1:
            k.type(word)
        # elif type(word) == list and word[0] in "Key.":
        #     word = eval(word[0])
        else:
            k.press(word)
            k.release(word)
        timer(1)

def func1(*words):
    from pynput.keyboard import Key,Controller
    k = Controller()
    for word in words:
        k.press(word)

def func2(*words):
    from pynput.keyboard import Key,Controller
    k = Controller()
    for word in words:
        k.release(word)

def timer(n):
    import time
    time.sleep(n)

n = 6
# while True:
timer(n)
# mouse.position = (782, 554)
# timer(n)
# mouse.click(Button.left,1)
# timer(n)
# mouse.position = (858, 386)
# mouse.click(Button.left,1)


for elem in range(21,9931):
    key(str(elem),Key.enter)
    
    
