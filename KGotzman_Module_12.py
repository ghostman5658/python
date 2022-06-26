# Kye Gotzman 10/7/2021 Module 12
# Purpose of the code is to improve a past program.
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.


class BankAccount:
  """A simple attempt to represent a BankAccount"""

  def __init__(self, account_number, balance):
    """Initialize the attributes to describe a bank account."""
    self.account_number = account_number
    self.balance = balance
    self.fees = 5
    self.minimum_balance = 50

  def make_withdrawal(self):
    """Subtract the amount from the balance."""
    print(f"\nThere is a ${self.fees} processing fee for this transaction.")
    go_nogo = input("Would you like to continue? (Y/N) ")
    go_nogo = go_nogo.upper()
    if go_nogo == ('Y'):
      withdrawal = input("Enter amount you want to withdraw from your account. ")
      if(self.balance >= int(withdrawal)):
        new_balance1 = self.balance - int(withdrawal) - self.fees
        print(f"\nWithdraw from account {self.account_number} of ${withdrawal} successful.")
        print(f"You now have ${new_balance1} in account {self.account_number}.")
        if new_balance1 < 50:
          print(f"Your account has less than the minimum required balance ${self.minimum_balance}, please deposit funds imidiately.")
        else:
          None 
        return new_balance1
      else:
        print(f"Could not withdraw ${withdrawal} from account {self.account_number} due to insufficient funds.")
    elif go_nogo == ('N'):
      return
    else:
      print("Invalid input, please input Y or N")

  def make_deposit(self):
    """Add the ammount to the balance."""
    deposit = input("Enter the amount you want to deposit into your account. ") 
    new_balance2 = self.balance + int(deposit)
    print(f"\nDeposit of ${deposit} to account {self.account_number} successful.")
    print(f"You now have ${new_balance2} in account {self.account_number}")
    return new_balance2

  def check_balance(self):
    """Show account balance and error if balance is below minimum"""
    print(f"\nThe current balance in account {self.account_number} is ${self.balance}")
    if self.balance < self.minimum_balance:
      return (f"\nYou do not have enough funds. The minimum account balance is ${self.minimum_balance} and your current balance is ${self.balance}. Please add funds.")
    else:
      None 


def manage_account(account):
  """Function to depict option menu similar to an ATM"""
  while True:
    print("\nAccount Options"
      "\n\t1 Check Account Balance"
      "\n\t2 Make Deposit"
      "\n\t3 Make Withdrawal"
      "\n\t4 Return")
    user_selection = input("Please choose from the above options and enter the number here: ")
    if (user_selection == '1'):
      account.check_balance()
    elif (user_selection == '2'):
      account.make_deposit()
    elif (user_selection == '3'):
      account.make_withdrawal()
    elif (user_selection == '4'):
      return
    else:
      print("Invalid Option")


user_account = BankAccount(1234, 200)
pin_nums = ['0000']
print("\nWelcome to Money Tree Bank!")

active = True
while active:
  user_pin = input("Enter Pin Number: ")
  for pin_num in pin_nums:
    if (user_pin) in pin_nums:
      manage_account(user_account)
    elif user_pin == 'q':
      active = False
    else:
      print("Invalid Pin Number")







