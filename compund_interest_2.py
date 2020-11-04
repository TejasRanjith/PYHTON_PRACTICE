print('''
        1. Principal Amount 
        2. Rate of Interest 
        3. Time Period in Year ''')
import functions
 
principleAmount = input("1. --> ")
rate = input("2. --> ")
term = int(input("3. --> "))
print('''Pmt.      |Payment Date  |  Beginning Balance    |  Scheduled  |  Extra Payement  |  Total Payment  |  Principal  |  Interest  |  Ending Balance  |  Cumalitive Interest  | 
 No.      |              |                       |   Payement  |                  |                 |             |            |                  |                       |''')
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
newPrincipleAmount = principleAmount
counter = 1 
while counter <= term:
        newPrincipleAmount = functions.compound_interest(newPrincipleAmount,rate,counter)
        counter+=1 
term2 = input("Mention the Time : ")
addoc = input("If you have any amount to reduce the principal, please mention the amount in the respective blank : ")
print(addoc,term2)
# functions.compound_interest(principleAmount,rate,term) 
 