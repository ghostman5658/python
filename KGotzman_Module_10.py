# Kye Gotzman 10/3/2021 Module 10
# Purpose of the code is read and write to a txt file and then check for accuracy.
# Matthes, E. 2019. Python Crash Course 2nd Edition, 
#“A Hands-On, Project-Based Introduction To Programming. 
#No Starch Press, Inc. San Francisco, CA.



file_location = input("Where would you like to save this file? (please ensure to use proper file structure) ")
file_name = input("what would you like to call your file? ")
filename = (f"{file_location.strip()}/{file_name.strip()}.txt")
  
def store_user_data():
  """Store user data to include name, address, and phone number to the selected file path."""
  name = input("What is your name? ")
  address = input("what is your address? ")
  phone_number = input("What is your phone number? ")
  user_data = (f"Name: {name.title()}\nAddress: {address}\nPhone Number: {phone_number}")
  with open(filename, 'w') as f:
    f.write(user_data)
  return user_data

def get_user_data():
  """Get stored user data if available."""
  with open(filename) as f:
    user_data = f.read()
    print(user_data)

active = True
while active:
  store_user_data()
  get_user_data()
  data_validation = input("Is that information correct?")
  if data_validation == 'y':
    break
  elif data_validation == 'Y':
    break
  elif data_validation == 'yes':
    break
  elif data_validation == 'Yes':
    break
  elif data_validation == 'YES':
    break


