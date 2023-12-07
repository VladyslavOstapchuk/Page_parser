from urllib.request import urlopen
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
import re

url = 'https://www.neo.space/blog/things-to-consider-for-creating-professional-email-address-examples-ideas'
url = 'https://www.w3schools.com/python/python_try_except.asp'

url_parts = urlsplit(url)

print()

def html_to_soup(url):
    # read all html text
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features='html.parser')

    return soup

def soup_to_text(soup):
    # kill all script and style elements
    for script in soup(['script','style']):
        script.extract() # rip it out

    # get text from html
    text = soup.get_text()
    text = re.split('\s+',text)

    return text

def html_to_text(url):
    return soup_to_text(html_to_soup(url))

# email gathering
def get_emails_from_text(text):
    emails = []

    # email regex
    pattern = r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,})'

    for word in text:
        match_object = re.match(pattern, word)
        if(match_object):
            # print(match_object.group())
            emails.append(match_object.group())

    return emails

def get_emails_from_html(url):
    return get_emails_from_text(html_to_text(url))
# save text
def save_to_file(lines, file_name):
# store all emails to the file
    if lines:
        with open(file_name, 'w') as f:
            for line in lines:
                f.write(line+'\n') 

# get contact page link
def get_contact_page(url):
    soup = html_to_soup(url)

    contact_page_names = ('contact','about','career','services')
    all_page_links = [a.attrs.get('href') for a in soup.select('a[href]') ]

    contact_pages = []
    for link in all_page_links:
        for name in contact_page_names:
            if name in link:
                contact_pages.append(link)
                break

    return contact_pages

# get emails from page with url
emails = get_emails_from_text(html_to_text(url))
if emails:
    print(f'\nEmails from page {url}:\n{emails}')

contact_pages = get_contact_page(url)

# print(contact_pages)
if contact_pages:
    for page in contact_pages:
        # if link doesn't contain relative path
        if not (page.startswith('http') or page.startswith('www')):
            # get url base
            base_url = url_parts.scheme + '://' + url_parts.netloc
            # append the part leading to the contact page
            page=base_url+page

        tmp = None

        # try to get emails from contact page
        try:
            tmp = get_emails_from_text(html_to_text(url))
            print(f'\nEmails from page {page}:\n{tmp}')
        except Exception:
            print(Exception)
        
        # if additional mails from contact page found add them to already found emails
        if tmp:
            emails.extend(tmp)

if emails:
    emails = set(emails)
    print(f'\nAll gathered emails:\n{tmp}')
    save_to_file(emails,'my_modified_email_crawler_result.txt')


exit(0)



