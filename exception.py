import time


while True:
    try:
        num = int(input('Enter an integer: '))
        print(f'>> {num}')
        break
    except ValueError:
        print('Try again')
        continue
time.sleep(3)
