# Kye Gotzman 8/26/2021 Module 4
# Purpose of the program is to display a Tupple in various ways
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.

western_states = ('washington','oregon','california','idaho','nevada','arizona','utah','montana','wyoming','colorado','new mexico','texas','oklahoma','kansas','nebraska','south dakota','north dakota')

print(western_states)

for western in western_states: 
	print(f"{western.title()} is in the Western half of the United States.")

a_z_states = list(western_states) #change tuple into list

a_z_states.sort() #sort list alphabetically

western_states = tuple(a_z_states) #convert list back into tuple

for western in western_states:
	print(f"{western.title()} is a state in the U.S.")
