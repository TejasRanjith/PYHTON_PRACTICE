#for i in range(0,1):
    #print("NOTHING")
    # Python handout
    # import os     #Bank_Management_System.py
    # os.system("python grp_app//Bank_Management_System.py")
    # os.system("python Rough.py")

    # to run another python file in this file. ↑↑↑

    # import re
    # s = "blahblah@yahoo.com"
    # domain = re.search("@[\w.]+", s)
    # print (domain.group())

    # to extract the domain part of an email. ↑↑↑

    # print(bin(-1))
    # it returns -0b1
    # import os
    # os.system("cmd")

    # import random
    # units = ["kg","g","mg","km","m","cm","mm","l","ml"]
    # decimal = [1,10,100]
    # i = 0
    # while i<=10:
    #     print(random.randint(100,999)/decimal[random.randrange(0,3)],units[random.randrange(0,9)])
    #     print()
    #     i+=1

    # import random
    # i = 0
    # while i <= 50:
    #     print(str(random.randint(2,9))+" X "+str(random.randint(2,9)))
    #     print()
    #     i+=1

    # import os
    
    # dir = 'C://Users//home//Desktop//Desktop (2)//Screenshots'
    # for files in os.listdir(dir):
    #     print(files)
    #     if ".png" in files:    
    #         os.remove(dir + "//"+ files)
    #     else:
    #         continue
    # handout: exclude
    # print(type(os.listdir(dir))) <class 'list'>
    # tup = 1,2,3
    # print(type(tup))
    # print(tup[:1]*5)
def countdown(t): 
    import time
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1



# countdown(5)
# from pynput.keyboard import Key, Controller
# keyboard = Controller()
# keyboard.press(Key.cmd_l)
# keyboard.press("s")
# keyboard.release(Key.cmd_l)
# keyboard.release("s")
