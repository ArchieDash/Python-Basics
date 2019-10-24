import time
import mechanicalsoup

url = 'http://olympus.realpython.org/dice'
browser = mechanicalsoup.Browser()
for trial in range(3):
    request = browser.get(url)
    roll = request.soup.select('#result')[0]
    trial = request.soup.select('#time')[0]
    timer = trial.text.split(' ')[3]
    print(f'Dice roll equals {roll.text} at {timer}')
    time.sleep(3)
