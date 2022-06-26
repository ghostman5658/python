# Bankaccount class and child classes with functions in each
 
class Bank_Account:
    def __init__(self, acctnumber, balance):
        self.acctnumber = acctnumber
        self.balance = balance
        print("\n Welcome to the Bank balance tracker")
 
#deposit function
    def Deposit(self):
        deposit=float(input("Enter amount to be deposited: "))
        self.balance += deposit
        print("\n You deposited $",deposit, " in account" , self.acctnumber, "your current balance is $", self.balance)
 
 #withdraw function
    def Withdraw(self):
        deduction=float(input("Enter amount to be withdrawn: "))
        if self.balance>=deduction:
            self.balance-=deduction
            print("\n You withdrew $" , deduction , " from your account number" , self.acctnumber)
        else:
            print("\n Your Account has an insufficient balance ")
 
#getbalance function
    def getBalance(self):
        print("\n Your avalable balance is $",self.balance, "in account number", self.acctnumber) 
 
 #child class
class CheckingAccount(Bank_Account):
    def __init__(self,acctnumber,balance,fees,min_balance):
        Bank_Account.__init__(self, acctnumber, balance)
        self.fees=fees
        self.min_balance=min_balance
 
    def checkminbalance(self):
        if self.balance < self.min_balance:
            print("\n Your account", self.acctnumber, "is below the minimum balance of $", self.min_balance)
       
    def deduct_fees(self):
        self.balance=self.balance-self.fees
        
  #child class      
class SavingsAccount(Bank_Account):
    def __init__(self,acctnumber,balance,interestrate):
        Bank_Account.__init__(self, acctnumber, balance)
        self.interestrate = interestrate
       
    def addinterest(self):
 
        self.balance=self.balance+(self.interestrate*100/self.balance)
        #self.balance=self.balance+1
        #print(self.balance)
      
      
bankaccount = Bank_Account(123456,200) 
bankaccount.Deposit()
bankaccount.Withdraw()
bankaccount.getBalance()     
if __name__ == "__main__":
 
  checkingacount = CheckingAccount(3456,25,5,50)
  try:
 
    checkingacount.checkminbalance()
    checkingacount.getBalance()
  except:
    print (" You did not enter 100 or 25")
    
#checkingacount.deduct_fees()
#checkingacount.getBalance()
 
  savingsaccount = SavingsAccount(78910,100,2)
  savingsaccount.getBalance()
  savingsaccount.addinterest()
  savingsaccount.getBalance()