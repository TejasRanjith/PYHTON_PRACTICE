import random,webbrowser
from pynput.keyboard import Key, Controller

k = Controller()

def timer(n):
    import time
    time.sleep(n)
    return n

def key(*words):
    for word in words:
        if type(word) == str and len(word) != 1:
            k.type(word)
        else:
            k.press(word)
            k.release(word)
        timer(1)

def func1(*words):
    for word in words:
        k.press(word)

def func2(*words):
    for word in words:
        k.release(word)

s,n = "",random.randint(0,10)
timer(0+n)
# key(Key.alt,Key.tab)
webbrowser.open_new_tab("https://www.youtube.com/watch?v=Pc-99lSRNfg")
key(Key.space)
func1(Key.alt,Key.tab)
func2(Key.alt,Key.tab)
for i in range(5):
    s+=str(random.randint(0,9))
print(s)
while True:
    put = input("-->>  ")
    if put == s:
        break

func1(Key.alt,Key.tab)
func2(Key.alt,Key.tab)
key(Key.space)