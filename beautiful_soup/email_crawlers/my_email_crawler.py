from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://www.neo.space/blog/things-to-consider-for-creating-professional-email-address-examples-ideas'
# url = 'https://www.bbc.com/news'

# read all html text
html = urlopen(url).read()
soup = BeautifulSoup(html, features='html.parser')

# kill all script and style elements
for script in soup(['script','style']):
    script.extract() # rip it out

# get text from html
text = soup.get_text()
text = re.split('\s+',text)

# email regex
pattern = r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,})'

# email gathering
emails = []

for word in text:
    match_object = re.match(pattern, word)
    if(match_object):
        print(match_object.group())
        emails.append(match_object.group())

# store all emails to the file
if emails:
    with open('my_emails.txt', 'w') as f:
        for email in emails:
            f.write(email+'\n') 

