#base class for all bank account types to inherit
class BankAccount():

	def __init__(self, accountNumber, balance):
		self.accountNumber = accountNumber
		self.balance = balance
	
	#get money from bank accounts
	def withdraw(self):
		amount = getPositiveInput("Please input the amount you wish to withdraw: ")
		if (self.balance >= amount):
			self.balance = self.balance - amount
			print(f"\nWithdraw of ${amount} successful")
		else:
			print(f"\nCould not withdraw ${amount}. Insufficent Funds")
		self.getbalance()
		return

	#add money to bank accounts
	def deposit(self):
		amount = getPositiveInput("Please input the amount you wish to deposit: ")
		self.balance += amount
		print(f"\nDeposit of ${amount} successful")
		self.getbalance()
		return

	def getbalance(self):
		print(f"\nCurrent Balance is ${self.balance}")
		return

'''
Definition - function for checking account actions
Arguments: account - the checking account object to be worked on
'''
def manageBankAccount(account):
	while True:
		print("\nAccount Options"
		"\n1. Get Account Balance"
		"\n2. Deposit"
		"\n3. Withdraw"
		"\n4. Return")
		selection = input("\nPlease input the number for your chosen action: ")
		if (selection == "1"):
			account.getbalance()
		elif(selection == "2"):
			account.deposit()
		elif(selection == "3"):
			account.withdraw()
		elif(selection == "4"):
			return
		else:
			print("\nInvalid input")

'''
Definition - function for geting a positive number with error checking
Arguments: statment - the statement to ask the user when asking for a number
'''
def getPositiveInput(statement):
	badInput = True #flag for catching bad inputs
	while(badInput):#While loop used to avoid Value Error if the user does not enter a valid number
		try:
			amount = float(input("\n" + statement))
			if amount < 0:
				print("Error, Please enter positive number")
			else:
				badInput = False
		except ValueError:
			print("Error, Please enter a positive number")
	return amount


#Program Start
#initialize Account
account01 = BankAccount(1001, 200)
#initial selection menu
print("\nWelcome to Python Bank")
manageBankAccount(account01)
#code end