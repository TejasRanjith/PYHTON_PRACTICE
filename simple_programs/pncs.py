from math import factorial
import functions
while 1 == 1:
    a = input("Permutation, or Combination ? --> ")
    a = a.lower()
    if a == "p":
        functions.permutation()
        break
    elif a == "c":
        functions.combination()
        break
    else:
        print("Invalid Option........")