# Kye Gotzman 8/26/2021 Module 3
# Purpose of the code is to calculate the cost of installing fiber optic cable
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.

print("Welcome to Fiber Calc")
company_name = input("What is your company name?")
fiber_feet = input("How many feet of fiber need to be installed?")
cost = float(fiber_feet) * .87 #convert fiber_feet into float in order to multiply
print(f"Total cost of install to {company_name} is ${cost}")