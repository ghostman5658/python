# Kye Gotzman 8/28/2021 Module 5
# Purpose of the code is to calculate the cost of installing fiber optic cable including bulk discounts
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.

print("Welcome to Fiber Calc")
company_name = input("What is your company name? ")
fiber_feet = input("How many feet of fiber need to be installed? ")
fiber_feet = float(fiber_feet)
if fiber_feet > 500:
	price = .5
elif fiber_feet > 250:
	price = .7
elif fiber_feet > 100:
	price = .8
elif fiber_feet <= 100:
	price = .87 
cost = float(fiber_feet) * float(price) #convert fiber_feet and price into float in order to multiply
print(f"Total cost of installing {fiber_feet}ft of fiber to {company_name} is ${cost}")