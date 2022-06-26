# Kye Gotzman 9/17/2021 Module 8
# Purpose of the code is to use a function to convert miles to kilometers.
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.


def miles_kilometers_conversion(miles):
  """Convert miles to kilometers"""
  kilometers = float(miles) * 1.60934
  return(kilometers)

miles = input('How many miles did you drive? ')

if miles == '1': 
  distance = 'mile'
else:
  distance = 'miles'

try:
  print(f"\nYou drove {miles} {distance} which is {miles_kilometers_conversion(miles)} kilometers.")
except:
  print(f"\nError - you must enter a number.")
