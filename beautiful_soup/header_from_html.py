import requests
from bs4 import BeautifulSoup

# page url
url = 'https://www.bbc.com/news'

# request and store the web page
response = requests.get(url)
# parse requested page
soup = BeautifulSoup(response.text, 'html.parser')
#
headlines = soup.find_all('h3',class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

for headline in headlines:
    print(headline.text.strip())
