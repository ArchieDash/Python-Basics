import time

while True:
    password = input('Tell me your password:').strip()
    try:
        print(f'The first letter you entered was: {password[0].upper()}')
        break
    except IndexError:
        continue
time.sleep(3)
