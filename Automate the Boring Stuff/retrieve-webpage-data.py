
# Goes to the Resourcive webpage and grabs a specific CSS Selector and then prints its different components
import requests, bs4

result = requests.get('https://www.resourcive.com')
try:
    result.raise_for_status()
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    element = soup.select('#hs_cos_wrapper_widget_1674752181380 > div > div > div.image-button-container > a')
    print(type(element)) 
    print(len(element))
    print(type(element[0]))
    print(str(element[0]))
    print(element[0].getText())
    print(element[0].attrs)


except Exception as err:
    print('An error happened: ' + str(err))
