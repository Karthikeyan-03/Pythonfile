#BASS CLASS
class Account:
    def __init__(self,name,balance,min_balance):  #CONSTRUCTOR
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):         #ADDING AMOUNT
        self.balance=self.balance+amount

    def withdraw(self,amount):        #WITHDRAW AMOUNT
        if self.balance-amount>=self.min_balance:       #CHECKING MIN BALANCE
            self.balance=self.balance-amount
        else:
            print("Sorry,Insufficent Balance")

    def printstatement(self):
        print("acc bal:",self.balance)

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=1000)    #USE BASE CLASS CONSTRACTOR VAR

    def __str__(self):
        return "{} current.accbal{}".format(self.name,self.balance)   #USED F STRING TO RETURN DATA

class Saving(Account):   #FOR SAVINGS ACCOUNT
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)

    def __str__(self):
        return "{} Saving Account With Balance {}".format(self.name,self.balance)

c=Saving("Karthi",10000)
print(c)
c.deposit(5000)
c.printstatement()
c.withdraw(16000)
c.withdraw(2000)
print(c)
c2=Current("Dharshan",20000)
c2.deposit(6000)
print(c2)
c2.withdraw(2000)
c2.withdraw(28000)
print(c2)
