import functions


functions

                                                                         # complete
try:
    principleAmountInt =round(int(150000),2)
    rateFloat= round(float(5),2)
    termInt = round(int(13),2)
    interestAmount = round(principleAmountInt * (rateFloat/100),2)
    rateTime = round((1 + rateFloat/100)**termInt,2)
    compountInterest =round(principleAmountInt *rateTime,2)
    lst = {'1' : str(termInt),'2': str(principleAmountInt),'3' : str(interestAmount),'4' : str(compountInterest)}
    
    print('''Pmt.      |Payment Date  |  Beginning Balance    |  Scheduled  |  Extra Payement  |  Total Payment  |  Principal  |  Interest  |  Ending Balance  |  Cumalitive Interest  |''')

    for value in lst:
        print(value)
except ValueError:
    print("Please enter a valid number")
