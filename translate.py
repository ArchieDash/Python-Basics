import time


string = input('Enter some text: ')
leetspeak = {
                'a':'4',
                'b':'8',
                'e':'3',
                'l':'1',
                'o':'0',
                's':'5',
                't':'7'
            }
for letter in string:
    if letter in leetspeak.keys():
         string = string.replace(letter, leetspeak[letter])
print(string)
time.sleep(3)
