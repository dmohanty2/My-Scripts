import requests
import re
from urllib.parse import urljoin


""" To Find all links inside the webpage using regex,requests,urllib.parse"""

link = "https://yourlink.com"

r=requests.get(link)  #using requests module to fetch the website as HTML

r.text

'''using regex module to find links as all will have 
standard href at the beginning'''

search_query = re.compile(r'href="(.*?)"')


links = search_query.findall(r.text)
print("\nFound {} links".format(len(links)))
list_of_links=[link]
for l in links:
    list_of_links.append(urljoin(link,l))
    
    
#print(list_of_links)
#used set to remove repeated links 
u_set_of_links = set(list_of_links)

print(u_set_of_links)

