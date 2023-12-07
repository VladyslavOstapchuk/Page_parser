import pandas as pd 
#to parse encoded urls
from urllib import parse

#link to the webpage
url = 'https://en.wikipedia.org/wiki/The_Mandalorian'

#read tables from html with pandas      
data = pd.read_html(url, encoding='utf-8')

#print all downloaded html data 
print(data[1])

#parse url from base64
url = parse.quote(url, safe=':/')
print(url)

#write tables from the web page to the xlsx file
with pd.ExcelWriter('tables_res.xlsx') as writer:
    for idx, df in enumerate(data):
        df.to_excel(writer, sheet_name=f'Table {idx}')


