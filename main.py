# Author:Gcobani Mkontwana
#date:27/02/2023
#Script scraps the website using request and beautifulSoup library

from google_translate import browser
from google_translate import selenium
import requests
from bs4 import BeautifulSoup
URL = "https://www.classcentral.com/?"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
r = requests.get(url=URL, headers=headers)
print(r.content)
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))

