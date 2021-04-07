


#* ---------------All-types-of-classes------------------------------------------------------------------------------------------------
    
    #?  -------------------Circle--------------------------------------------------------------------
        # class Circle():
        #     pi = 22/7
        #     def __init__(self,radius = 1):
        #         self.radius = radius
        #         self.area = (radius**2)*self.pi
        #     def circumference(self):
        #         return self.radius * self.pi * 2



        # var = Circle(7)
        # print(var.pi)
        # print(var.radius)
        # print(var.area)
        # print(var.circumference())
    
    #?  -------------------Animal--------------------------------------------------------------------
        # class Animal():
        #     def __init__(self):
        #         print("Animal Created.")
            
        #     def who_am_i(self):
        #         print("I am an Animal.")
            
        #     def eat(self):
        #         print("I am Eating.")

        # class Dog(Animal):
        #     def __init__(self):
        #         Animal.__init__(self)
        #         print("Dog created")



        # var = Dog()

    #?  -------------------Book----------------------------------------------------------------------
        # class Book():
        #     def __init__(self,name,author,pages):
        #         self.name = name
        #         self.author = author
        #         self.pages = pages
            
        #     def __len__(self):
        #         return self.pages
            
        #     def __str__(self):
        #         return f"{self.name} by {self.author}"


        # var = Book("Python","Tejas",200)
        # print(str(var))
    
    #?  -------------------Line----------------------------------------------------------------------
        # class Line():
            
        #     def __init__(self,coor1,coor2):
        #             self.x1,self.y1,self.x2,self.y2 = coor1[0],coor1[1],coor2[0],coor2[1] 
        #     def distance(self):
        #         return (((self.x2-self.x1)**2) + ((self.y2-self.y1)**2))**(1/2)
            
        #     def slope(self):
        #         return ((self.y2-self.y1)/(self.x2-self.x1))

        # var = Line((3,2),(8,10))
        # print(var.distance())
        # print(var.slope())
    
    #?  -------------------Cylinder------------------------------------------------------------------
        # class Cylinder():
        #     pi = 3.14
            
        #     def __init__(self,height=1,radius=1):
        #         self.height = height
        #         self.radius = radius
                
        #     def volume(self):
        #         return (self.pi) * (self.radius)**2 * (self.height)
            
        #     def surface_area(self):
        #         return (2*(self.pi)*(self.radius)*(self.height))+(2*(self.pi)*(self.radius) ** 2)


        # var = Cylinder(2,3)
        # print(var.volume())
        # print(var.surface_area())
    
    #?  -------------------Bank-Account--------------------------------------------------------------
        # class Account():
        #     def __init__(self,owner,bal):
        #         self.owner = owner
        #         self.bal = bal
            
        #     def deposit(self,add):
        #         self.bal = self.bal + add
        #         return self.bal
            
        #     def withdraw(self,sub):
        #         if sub >= self.bal:
        #             print("Cannot withdraw as it exceeds the balance,",self.bal)
        #         elif sub == 0:
        #             print("Cannot Withdraw 0 amount !!")
        #         else:
        #             self.bal = self.bal - sub
        #             return self.bal
            
        #     def __str__(self):
        #         return f'''
        #         Account Owner : {self.owner}
        #         Account Balance : {self.bal}'''

        # acct1 = Account('Jose',100)
        # print(acct1)
        # print(acct1.owner)
        # print(acct1.bal)
        # print(acct1.deposit(50))
        # print(acct1.withdraw(75))
        # print(acct1.withdraw(500))
        # print(acct1)

    #?  ---------------------------------------------------------------------------------------------



#* ---------------Error-Handling---------------------------------------------------------------------------------------------

    #?  -------------------TRY=EXCEPT=ELSE=FINALLY---------------------------------------------------
        # try:
        #     result = 10 + "10"
        #     print("TRY BLOCK")
        # except:
        #     print("EXCEPT BLOCK")
        # else:
        #     print("SUCCESFUL ELSE BLOCK")
        # finally:
        #     print("FINAL BLOCK")

    #?  -------------------Homework1-----------------------------------------------------------------
        # try:
        #     for i in ['a','b','c']:
        #         print(i**2)
        # except:
        #     print("You cannot use exponents on words. Only on numbers.")
        # else:
        #     print("Program executed properly.")

    #?  -------------------Homework2-----------------------------------------------------------------
        # try:
        #     x = 5
        #     y = 0
        #     z = x/y
        #     print(z)
        # except:
        #     print("You cannot divide any number by zero.")
        # else:
        #     print("All done.")

    #?  -------------------Homework3-----------------------------------------------------------------
        # def ask():
        #     while True:
        #         try:
        #             num = int(input("Provide a Number : "))
        #             print(num**2)
        #         except:
        #             print("Please provide a number.")
        #         else:
        #             print("Code completed succesfully.")
        #             break

        # ask()

    #?  ---------------------------------------------------------------------------------------------


