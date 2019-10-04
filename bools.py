import time


string = input('Type some string: ')
if len(string) > 5:
    print('Lenght of the string is greater than 5 chars.')
elif len(string) < 5:
    print('Lenght of the string is less than 5 chars.')
else:
    print('Lenght of the string is equal to 5 chars.')
time.sleep(3)
