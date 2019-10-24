import mechanicalsoup as mechsoup


url = 'http://olympus.realpython.org/login'
browser = mechsoup.Browser()
html = browser.get(url).soup
form = html.select('form')[0]

form.select('input')[0]['value'] = 'zeus'
form.select('input')[1]['value'] = 'ThunderDude'
profiles_page = browser.submit(form, url)
title = profiles_page.soup.find('title').get_text()
print(f'\nCurrent page: {title}\n')

form.select('input')[0]['value'] = 'user'
form.select('input')[1]['value'] = 'Password'
profiles_page = browser.submit(form, url)
print(profiles_page.soup) # wrong username or password!
