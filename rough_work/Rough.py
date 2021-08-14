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
# def countdown(t): 
#     import time
#     while t: 
#         mins, secs = divmod(t, 60) 
#         timer = '{:02d}:{:02d}'.format(mins, secs) 
#         print(timer, end="\r") 
#         time.sleep(1) 
#         t -= 1



# countdown(5)
# from pynput.keyboard import Key, Controller
# keyboard = Controller()
# keyboard.press(Key.cmd_l)
# keyboard.press("s")
# keyboard.release(Key.cmd_l)
# keyboard.release("s")


# import webbrowser
# google = input('Google search:')
# webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=' + google)
# #to search google 


# string = "tejas@gmail.com"
# name = string.partition("@")[0]
# domain = string.partition("@")[-1]
# print("domain name","name","domain")
# print(domain.partition(".")[0],name,domain)

# print(divmod(9,4))

# d1 = {'k0': 0,'k1':1,'k2':2,'k3':3,'k4':4,'k5':5,'k6':6,'k7':7,'k8':8,'k9':9}
# da = {'ka':'a','kb':'b','kc':'c','kd':'d','ke':'e','kf':'f','kg':'g','kh':'h','ki':'i','kj':'j','kk':'k','kl':'l','km':'m','kn':'n','ko':'o','kp':'p','kq':'q','kr':'r','ks':'s','kt':'t','ku':'u','kv':'v','kw':'w','kx':'x','ky':'y','kz':'z'}
# for elem in d1:
#     print(d1[elem],end = "")

# Python program to print all permutations with 
# duplicates allowed 
  
# def toString(List): 
#     return ''.join(List) 
  
# # Function to print permutations of string 
# # This function takes three parameters: 
# # 1. String 
# # 2. Starting index of the string 
# # 3. Ending index of the string. 
# def permute(a, l, r): 
#     if l == r: 
#         print toString(a) 
#     else: 
#         for i in xrange(l, r + 1): 
#             a[l], a[i] = a[i], a[l] 
#             permute(a, l + 1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack 
  
# # Driver program to test the above function 
# string = "ABC"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n-1) 
  
# # This code is contributed by Bhavya Jain 

# Code for renaming screenshots file
# import os
# dir = 'C://Users//home//Desktop//Desktop (2)//Screenshots'
# for files in os.listdir(dir):
#     print(files)
#     for i in range(1,51):
#         if files == f"Screenshot ({i}).png":
#             print(True)
#             os.rename(dir+f"//Screenshot ({i}).png",dir+f"//Screenshot ({i+4700}).png")
#         else:
#             continue
    

# import stdiomask as sm
# print(sm.getpass())
#.r OUTPUT ==>>
#.y Password: ***
#.y 123

# from geopy.geocoders import Nominatim
  
# # calling the nominatim tool
# geoLoc = Nominatim(user_agent="GetLoc")
  
# # passing the coordinates
# locname = geoLoc.reverse("25.3374, 55.4121")
  
# # printing the address/location name
# print(locname.address)