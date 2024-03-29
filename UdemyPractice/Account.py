class Account():
    def __init__(self, owner, bal):
        self.owner = owner
        self.bal = bal

    def deposit(self, add):
        self.bal = self.bal + add
        return self.bal

    def withdraw(self, sub):
        if sub >= self.bal:
            print("Cannot withdraw as it exceeds the balance,", self.bal)
        elif sub == 0:
            print("Cannot Withdraw 0 amount !!")
        else:
            self.bal = self.bal - sub
            return self.bal

    def __str__(self):
        return f'''
        Account Owner : {self.owner}
        Account Balance : {self.bal}'''


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.bal)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))
print(acct1)
