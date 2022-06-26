# Dictionary of RE Factors

re_factor = {
	'FLSC': 1.5,
	'ECT': 1.25,
	'Sheet Explosive': 1.66,
	'Det Cord': 1.66,
	'Blasting Cap': 1.6,
	'C-4': 1.34,
	'Cratering Charge': .42,
	'Dynamite': .92,
	'M2': 1.17,
	'Banagalore': 1.17,
	'WG 20 Booster': 1.66, 
}

explosives = ['FLSC','ECT','Sheet Explosive','Det Cord','Blasting Cap','C-4','Cratering Charge','Dynamite','M2','Banagalore','WG 20 Booster']

new = 'qty' * 'weight' * 'ref' 

explosive = input('What explosive material did you use?')

qty = input('What was the quantity of the explosive used?')

if explosive == 'FLSC':
	'ref' = 1.5
	''