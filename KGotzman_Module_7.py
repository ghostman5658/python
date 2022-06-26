# Kye Gotzman 9/11/2021 Module 7
# Purpose of the code is to use a while loop to determine how many years it takes to double an investment.
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.


initial_investment = input('How much is your investment? ')
annual_interest_rate = input('What is the annual interest rate? ')

initial_investment2 = float(initial_investment)
annual_interest_rate2 = float(annual_interest_rate) / 100 

double_investment = initial_investment2 * 2
years = 0

while initial_investment2 <= double_investment:
  initial_investment2 = initial_investment2 * annual_interest_rate2 + initial_investment2
  years = years + 1

print(f'\nIf you invest ${initial_investment} at {annual_interest_rate}% annual interest it will take {years} years to double your investment.')




