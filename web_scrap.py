import re
from urllib.request import urlopen


url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode('utf-8')
with open('files/dionysus.html', 'w') as raw_html:
    for row in html:
        raw_html.write(row)

pattern = 'name:.*<'
search = re.search(pattern, html, re.IGNORECASE)#returns re.Match object
name = search.group() #extract string from re.Match
name = re.sub('<', '', name)
print(name.strip())

pattern = 'favorite color:.*'
search = re.search(pattern, html, re.IGNORECASE) #returns re.Match object
color = search.group() #extract string from re.Match
print(color.strip())
