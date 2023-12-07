import requests
import re
from bs4 import BeautifulSoup

# all found links
allLinks = []
# found mails
mails=[]

# crawled url 
url = 'https://www.neo.space/blog/things-to-consider-for-creating-professional-email-address-examples-ideas'
url = 'https://www.bbc.com/news'

# get page
response = requests.get(url)

# parse html page
soup = BeautifulSoup(response.text,'html.parser')

# get all links from the page
links = [a.attrs.get('href') for a in soup.select('a[href]') ]

# check other subpages form resource for contact info 
for i in links:
    if(("contact" in i or "Contact")or("Career" in i or "career" in i))or('about' in i or "About" in i)or('Services' in i or 'services' in i):
        allLinks.append(i)

# remove page link duplicates 
allLinks=set(allLinks)

# find email function
def findMails(soup):
    for name in soup.find_all('a'):
        if(name is not None):
            emailText=name.text
            match=bool(re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',emailText))
            if('@' in emailText and match==True):
                emailText=emailText.replace(" ",'').replace('\r','')
                emailText=emailText.replace('\n','').replace('\t','')
                if(len(mails)==0)or(emailText not in mails):
                    print(emailText)
                mails.append(emailText)

for link in allLinks:
    if(link.startswith("http") or link.startswith("www")):
        r=requests.get(link)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')
        findMails(soup)

    else:
        newurl=url+link
        r=requests.get(newurl)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')
        findMails(soup)

# remove duplicates
mails=set(mails)

with open("emails.txt","w") as f:
    for email in mails:
        f.write(email+'\n')

if(len(mails)==0):
    print("NO MAILS FOUND")