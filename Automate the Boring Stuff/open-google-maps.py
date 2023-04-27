
# Asks a user what address they want to see and then opens google maps and takes them to the address
import webbrowser as wb

address = input('what address do you want to see?')

gm = 'https://www.google.com/maps/place/'

wb.open(gm + address)
