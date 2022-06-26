
def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted"""
  full_name = f'{first_name} {last_name}'
  return full_name.title()

while True: 
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")

  f_name = input("First name: ")
  if f_name == 'q':
    break
  l_name = input("Last name: ")
  if l_name == 'q': 
    break

  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\nHello, {formatted_name}!")

def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = f"Hello, {name.title()}!"
    print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to completed_models after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Show all the models that were printed."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(*toppings):
  """Print the list of toppings that have been requested"""
  print(toppings)

make_pizza('peppernoi')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_pizza('peppernoi')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first 
  user_info['last_name'] = last 
  return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


class Dog:
  """A simple attempt to model a dog."""

  def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age 

  def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")










