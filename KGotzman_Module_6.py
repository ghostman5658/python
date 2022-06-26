# Kye Gotzman 9/4/2021 Module 6
# Purpose of the code is to demonstrate a dictionary by picking a favorite sports team
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.


pac_12 = {
	'utah': 'utes',
	'oregon': 'ducks',
	'usc': 'trojans',
	'oregon state': 'beavers',
	'arizona state': 'sun devils',
	'washington': 'huskies',
	'colorado': 'buffaloes',
	'california': 'golden bears',
	'ucla': 'bruins',
	'arizona': 'wildcats',
	'stanford': 'cardinals',
}
for state, teams in pac_12.items():
	print(state.upper()) #convert all keys to upper case for standardized format

favorite_team = input("What is your favorite Pac 12 team? ")
favorite_team = favorite_team.lower() #convert input to lower case to be able to interact with dictionary


if favorite_team in pac_12:
	team = pac_12[favorite_team].upper()
	print(f"Your favorite Pac 12 team is the:\n\t{favorite_team.upper()} {team}.")
else:
	print("That's not a Pac 12 team.")
