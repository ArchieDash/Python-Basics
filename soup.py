import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'http://olympus.realpython.org/profiles'
page = urlopen(url)
html = page.read().decode('utf-8')

with open ('index.html', 'w') as raw_html:
    for row in html:
        raw_html.write(row)

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link['href'])

profiles = [link['href'] for link in links]
for profile in profiles:
    page = urllib.parse.urljoin(url, profile)
    html = urlopen(page).read().decode('utf-8')
    print(BeautifulSoup(html, 'html.parser').get_text()
