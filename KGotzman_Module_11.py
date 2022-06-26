# Kye Gotzman 10/2/2021 Module 11
# Purpose of the code is to introduce a simple bug into the program.
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.


print("Welcome to Bro's pizzaria!")

requested_toppings = input("What toppings do you want on your pizza? ").split()

requested_toppings = list(requested_toppings)


available_toppings = ['pepperoni','cheese','mushrooms','olives','onions','green peppers','pineapple','ham','bacon']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings: 
		print(f"Adding {requested_topping}.")
	else
		print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")








