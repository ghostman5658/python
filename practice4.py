
account_number = ['1234', '5678']
username_password = {'kyle': 'ghost'}

input_account_number = input('What is your account number?')

if input_account_number in account_number:
  input_username = input('What is your username?')
  input_password = input('What is your password?')

else:
  print('That is an incorrect account number.')

if input_username and input_password in username_password:
  print('What would you like to do?')

else:
  print('That username and password is incorrect.')















