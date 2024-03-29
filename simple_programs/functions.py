# complete
def bin_convert (n) :                                                                                    
    try:
        x = bin(int(n))
        print(x)
    except ValueError :
        print(f"{n} is not a number so please enter a valid number.")    

# complete
def sum_of_n_squares(n) :                                                                                
    try:
        sm = 0
        for i in range(1, n+1) : 
            sm = sm + (i * i) 
        print(sm)
    except ValueError :
        print(f"{n} is not a number so please enter a valid number.")

# complete
def compound_interest(principleAmount,rate,term) :                                                                           
    try:
        principleAmountInt =round(int(principleAmount),2)
        rateFloat= round(float(rate),2)
        termInt = round(int(term),2)
        interestAmount = round(principleAmountInt * (rateFloat/100),2)
        rateTime = round((1 + rateFloat/100)**termInt,2)
        compountInterest =round(principleAmountInt *rateTime,2)
        print(str(termInt)+ '\t  | \t' + str(principleAmountInt) + '                                 \t \t|  \t ' + str(interestAmount) +'                                  \t |\t  \t ' + str(compountInterest))
        return compountInterest
    except ValueError:
        print("Please enter a valid number")

# complete
def circle_properties(r):                                                                                
    try:
        r1 = int(r)
        ar = 22/7 * r1 * r1
        pr = 2 * 22/7 * r1
        print(f"Therefore the area of the circle is {ar} and perimeter is {pr}")
    except ValueError : 
        print("Please mention a valid number")

# complete
def swapList(list):                                                                                      
      
    start, *middle, end = list
    list = [end, *middle, start] 
    return list
# complete
def numbers_between(start1,end1):                                                                        
    try:
        start = int(start1)
        end   = int(end1)
        for n in range(start + 1 , end):
            print(n)
    except ValueError:
        print("Please enter a valid number.")

# complete
def square_properties(a1):                                                                               
    try:
        a = int(a1)
        ar = a**2
        pr = 4*a
        print(f"The area of the square is {ar} and the perimeter of the square is {pr}.")
    except ValueError:
        print("Please enter a valid number.")

# complete
def cube_properties(a1):                                                                                 
    try:
        a = int(a1)
        tsa = 6*a
        v = a**3
        print(f"The Total Surface Area of the cube is {tsa} and the volume of the cube is {v}.")
    except ValueError:
        print("Please enter a valid number.")

# complete
def rectangle_properties(l1,b1):                                                                         
    try:
        l = int(l1)
        b = int(b1)
        ar = l*b
        pr = 2*(l+b)
        print(f"The area of the rectangle is {ar} and the perimeter of the rectangle is {pr}.")
    except ValueError:
        print("Please enter a valid number.")

# complete
def cuboid_properties(l1,b1,h1):                                                                         
    try:
        l = int(l1)
        b = int(b1)
        h = int(h1)
        tsa = 2*(l*b + b*h + h*l)
        v = l*b*h
        print(f"The Total Surface Area of the cuboid is {tsa} and Volume of the cuboid is {v}.")
    except ValueError:
        print("Please enter a valid number.")

# complete
def simple_interest(p1,r1,t1):                                                                          
    try:
        p = int(p1)
        r = float(r1)
        t = int(t1)
        si = p*r*t/100
        print(f"The simple interest of the following data, {p} , {r} and {t} is {si}.")
    except ValueError:
        print("Please enter a valid number.")

# complete
def triangle_properties(a1,b1,c1):                                                                      
    try:
        a = int(a1)
        b = int(b1)
        c = int(c1)
        pr = a + b + c
        s = pr/2
        in_root = s*(s-a)*(s-b)*(s-c)
        ar = (in_root)**1/2
        print(f"The perimeter and the area of the the triangle of sides {a},{b} and {c} are {pr} and {ar} respectively.")
    except ValueError:
        print("Please enter a valid number.")

# complete
def differentiation(c1,v1,p1):
    try:
        c = int(c1)
        v = v1
        p = int(p1)
        new_c = c * p
        new_p = p - 1
        print("                                                                         ")
        print("     Differentiation")
        print("Differentiated Coeffecient is",new_c)
        print("The variable used is",v)
        print("Differentiated Power is",new_p)
    except ValueError:
        print("Please enter a valid number.")

# complete
def result():
    a = ""
    x = input("--> ")
    a=a+x
    return a

# complete
def file_opening():
    f = open("TEST.txt","a")
    element = result() 
    f.write(element+"\n")
    f.close()

# complete
def file_reader():
    file_name = input("File Name --> ")
    f = open(file_name,"r")
    contents = f.read()
    print(contents)
    f.close()
    return contents

# complete
def file_clear():
    file_name = input("File to be cleared --> ")
    f = open(file_name,"w")
    f.write("")
    f.close()

# complete
def dice():
    import random
    num = random.randrange(1,7)
    return num

# complete
def toss():
    import random
    l  = ["heads","tails"]
    num = random.randrange(0,2)
    return l[num]


def datatypefuncs():
    while 1==1:
        print()
        print()
        print("0 to exit")
        a = eval(input("data type --> "))
        print()
        for elem in dir(a):
            # print(elem)
            if "_" not in elem:
                print(elem)
            else:
                pass
        else:
            break


def permutation():
    from math import factorial
    n = int(input('N --> '))
    r = int(input("R --> "))
    print("Permutation required:",int(factorial(n)/factorial(n-r)))


def combination():
    from math import factorial
    n = int(input('N --> '))
    r = int(input("R --> "))
    print("Combination required:",int(factorial(n)/(factorial(r)*factorial(n-r))))