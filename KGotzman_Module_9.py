# Kye Gotzman 9/26/2021 Module 9
# Purpose of the code is to use a class and the inheritance model to mimic a bank program.
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.


class BankAccount:
  """A simple attempt to represent a BankAccount"""

  def __init__(self, account_number, balance):
    """Initialize the attributes to describe a bank account."""
    self.account_number = account_number
    self.balance = balance

  def make_withdrawal(self, withdrawal):
    """Subtract the amount from the balance."""
    new_balance1 = self.balance - withdrawal
    return new_balance1

  def make_deposit(self, deposit):
    """Add the ammount to the balance.""" 
    new_balance2 = self.balance + deposit
    return new_balance2

  def get_balance(self):
    """Return a statement showing the balance."""
    the_balance = (f"The balance of account #{self.account_number} is ${self.balance}.")
    return the_balance

class CheckingAccount(BankAccount):
  """Represents aspects of a bank account specific to a checking account."""

  def __init__(self, account_number, balance):
    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to a checking account.
    """
    super().__init__(account_number, balance)
    self.fees = 5
    self.minimum_balance = 50

  def deduct_fees(self):
    """Return balance after deducting fees"""
    new_balance3 = self.balance - self.fees
    return new_balance3

  def check_minimum_balance(self):
    """Show account balance and error if balance is below minimum"""
    if self.balance < self.minimum_balance:
      return (f"\nYou do not have enough funds. The minimum account balance is ${self.minimum_balance} and your current balance is ${self.balance}. Please add funds.")

    else:
      return (f"\nYour account balance is ${self.balance}.")

class SavingsAccount(BankAccount):
  """Represents aspects of a bank account specific to a checking account."""

  def __init__(self, account_number, balance):
    """
    Initialize attributes of the parent class.
    Then initialie attributes specific to a checking account.
    """
    super().__init__(account_number, balance)
    self.interest_rate = .02

  def add_interest(self):
    """Return new balance with applied interest"""
    new_balance4 = self.balance * self.interest_rate + self.balance
    return new_balance4

my_bankaccount1 = CheckingAccount('1234', 200)
my_bankaccount2 = SavingsAccount('1234', 200)
my_bankaccount3 = CheckingAccount('5678', 25)
my_bankaccount4 = SavingsAccount('5678', 25)

print(f"If you withdraw $50 from your account, your ballance will be ${my_bankaccount1.make_withdrawal(50)}.")
print(f"If you deposit $50 to your account, your ballance will be ${my_bankaccount1.make_deposit(50)}.")
print(my_bankaccount1.get_balance())
print(my_bankaccount1.check_minimum_balance())

print(f"\nIf you withdraw $50 from your account, your ballance will be ${my_bankaccount3.make_withdrawal(50)}.")
print(f"If you deposit $50 to your account, your ballance will be ${my_bankaccount3.make_deposit(50)}.")
print(my_bankaccount3.get_balance())
print(my_bankaccount3.check_minimum_balance())

