print('''
        1. Principal Amount 
        2. Rate of Interest 
        3. Time Period in Year ''')
import functions

principleAmount = input("1. --> ")
rate = input("2. --> ")
term = int(input("3. --> "))
print("Year            Principal       Interest        Total")
print("--------------------------------------------------------")
newPrincipleAmount = principleAmount
counter = 1 
while counter <= term:
        newPrincipleAmount = functions.compound_interest(newPrincipleAmount,rate,counter)
        counter+=1 


# functions.compound_interest(principleAmount,rate,term)


