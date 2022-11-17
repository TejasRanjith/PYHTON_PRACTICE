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
# f = open("text.txt","w")
# f.write('''Smiling is infectious,
# You catch it like the flu.
# When someone smiled at me today,
# I started smiling too.''')
# f.close()
# f = open("text.txt","r")
# # contents = f.read()
# print(f.read(7))
# f.seek(2,0)
# print(f.read(3))



# f = open("text.txt","r")
# print(f.readlines())

# import csv
# with open("abc.csv","x",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["a","b","c"])
#     writer.writerow(["1","2","3"])
#     writer.writerow(["4","5","6"])
#     writer.writerow(["7","8","9"])

# with open("abc.csv","r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# f = open("text.txt")
# print(f.name)
# print(f.read(30))

# print("abc\r12")
# print("abc\r1234")


# l1 = [1,2,3]
# l2 = ["a","b","c","d"]
# d = dict(zip(l1,l2))
# print(d)


# str2 = "w"
# print("*".join(str1))
# print(str1)

# str2 = "abcd"
# print(3/10 == 0.1+0.2)
# print(s.find("e"))

# def count():
#     vow=0
#     f=open("text.txt", "r")
#     N=f.read()
#     M=N.split()
#     for i in M:
#         if(i=="a" or i== "e" or i=="i" or i=="o" or i=="u"):
#             vow=vow+1
#     print(vow)
#     f.close()
# count()


#sanjay if you can see this just type under this comment ok ?
# -->

# print("True:",int(True))
# print("False:",int(False))
# l = [5,4,9,6,2,3]
# for i in range(1,6): #.r 1,2,3,4,5
    # l[i] = l[i]-1
#.y L: [4,9,6,2,3,3]
# for i in range(0,6):
    # print(l[i],end = " ")

#make a funtion for printing the list in form of table

# rows  = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #.y 26
# colums = [1,2,3,4,5,6,7,8,9,10]
# for elem in rows:
    # print(elem,end = " ")
# print(end="\n")
# for elem in colums:
#     # print(elem)
# def foo():
#     total+=1
#     return total
# total = 0
# print(foo())

# def a(b):
#     b = b+[5] #.y Statement 2
#     # print(b)
#     # return b
# c = [1,2,3,4]
# # b = a(c)
# a(c)
# print(len(c),c)
# # print(len(b))


# def l(a):
#     print('a    ',a)
#     a[1] = 20
#     a = a+[10]
#     a+=[100]
#     a.append(1000)
#     print("Edited a     ",a)
# b = [1,2,3]
# print('b     ',b)

# l(b)
# print('b after fn call  ',b)

# def f1():
#     x = 100
#     print(x)
# x+=1
# f1()
# x=+1
# print(x)


# str1="Exam2021" #.r 8
# str2=""
# l=0
# while l < len (str1):
#     if str1 [l] >= "A" and str1[l] <= "M":
#         str2=str2+str1[l+1]
    
#     elif str1[l] >="0" and str1[l] <="9":
#         str2 = str2+str1[l-1]
#     else:
#         str2=str2+"*"
#     l=l+1
#     print(str2)  #.y x***m2
    
    
    

# def func(l):
    # l += [10]
    # l.append(20)
    # l = l+[30]

# x = [1,2,3]
# func(x)
# print(x)

# i=0
# def change(i):
#     i=i+1
#     return i
# change(1)
# print(i)

# a=[18, 23, 69, [73]]
# b=list(a)
# a[3][0]=110
# a[1]=34
# print (b)
# print(id(a[3]),"  ",a[3])
# print(id(b[3]),"  ",a[3])
# import copy
# print(dir(copy))

# i = 1
# while (i <= 10):
    # sum = 0
    # for x in range(1,i+1):
        # sum += x
    # print(i, sum)
    # i+=1
# for i in range(1,100):
    # if (i % 3 == 0) or (i % 4 == 0):
        # continue
    # print(i)

# l = [1,2,3]
# def change(l):
#     l = l+[4]
#     #.g l += [4]
#     print(l)

# change(l)
# print(l)
# l = l+[4,9]
# print(l)
# print(l+[100])
# p = 40
# r = 50
# p = p + r
# r = p - r
# p = p - r
# print (p, r)
# def phone_with_country_code (phone_number, country="India"):
#     country_codes = {"India": "+91", "Singapore": "+65", "United States": "+1"}
#     if country not in country_codes:
#         return("Country is not supported")
#     return (country_codes[country] + " " + phone_number)
# print(phone_with_country_code("9876500001"), "|", phone_with_country_code("203-607-1232", "United States"))

# str1 = "My name is Tejas and I am from India"
# print(str1.split(sep=" ", maxsplit=-1))

# p = 1
# q = 6
# def change_values():
#     global p
#     q = 5
#     p = p + q
#     return (p)
# change_values()
# print(p, q)
# import csv
# print("Enter your name and roll number to see your subject marks...\n")
# name = input("Enter Name exactly as in Hall Ticket: ")
# rollno = input("Enter Roll No.: ")
# with open('student_marks.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     match_found = False
#     for row in csv_reader:
#         line_count += 1
#         if line_count == 1:
#         #.r --->
#             pass
#         else:
#             if row[0].lower() == name.lower() and row[1] == rollno:
#                 match_found = True
#                 eng_marks = row[3]
#                 maths_marks = row[4]
#                 cs_marks = row[5]
#                 print("\n"+row[0]+"'s marks are:\nEnglish:",eng_marks)
#                 print("Maths:", maths_marks, "\nComp Sc:", cs_marks,"\n\nThank you!")
# if match_found == False:
#     print ("\nNo matching name and roll number found. Please check and re-enter")

# a dictinary of numbers in words from 1 to 100
dict_num_words = {
    "0":"zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
    "100": "hundred",
    "1000": "thousand"
    # "10000": "ten thousand",
    # "100000": "hundred thousand",
    # "1000000": "million",
    # "10000000": "ten million",
    # "100000000": "hundred million",
    # "1000000000": "billion",
    # "10000000000": "ten billion",
    # "100000000000": "hundred billion",
    # "1000000000000": "trillion",
    # "10000000000000": "ten trillion",
    # "100000000000000": "hundred trillion",
    # "1000000000000000": "quadrillion",
    # "10000000000000000": "ten quadrillion",
    # "100000000000000000": "hundred quadrillion",
    # "1000000000000000000": "quintillion",
    # "10000000000000000000": "ten quintillion",
    # "100000000000000000000": "hundred quintillion",
    # "1000000000000000000000": "sextillion"
}
# i = 0
# while True:
#     num_str = input("Number in string format: ")
#     if num_str == "0":
#         print(0)
#     else:
#         pass
#     num_list = list(num_str)
#     num_list.reverse()
#     new_num_list = []
#     new_num_str = 0
#     for i in range(len(num_list)):
#         new_num_list.append(num_list[i]+"0"*i)
#     # print(new_num_list)
#     new_tup = tuple()
#     keys = list(dict_num_words.keys())[28:]
#     main_keys = keys.copy()
#     keys.reverse();keys.extend(["10","1"]);keys.reverse()
#     # print(keys)
#     for i in range(len(new_num_list)):
#         if int(new_num_list[i]) == 0:
#             continue
#         else:
#             if new_num_list[i] in main_keys:
#                 new_tup+= (dict_num_words[new_num_list[i]],)
#             elif int(new_num_list[i]) % int(keys[i]) == 0 and keys[i] in main_keys:
#                 # print(new_num_list[i],keys[i])
#                 new_tup += (dict_num_words[keys[i]],dict_num_words[str(int(new_num_list[i]) // int(keys[i]))])
#             else:
#                 new_tup += (dict_num_words[new_num_list[i]],)
#     new_list = list(new_tup)
#     new_list.reverse()
#     result = ' '.join(new_list)
#     print(result)
    # i+=1
# input("Press Enter to exit")
# for i in range(len(new_num_list)):
#     if int(new_num_list[i]) % int(list(dict_num_words.keys())[i+29]) == 0:
#         print(str(num//100), dict_num_words[dict_num_words.keys()[i+29]])
# n = int(input('Number --> '))
# f=1
# for l in range(1,n+1):
#     f=f*l
# print("The factorial of",n,"is",f)


# d = {25:["a","b","c"],56:["d","e","f"],34:["g","h","i"]}

# for key in d:
#     for elem in d[key]:
#         print(elem,end=" ")
#     print()

