import time


while True:
    try:
      num = int(input('Enter a positive integer: '))
      if num > 0:
        break
      else:
        continue
    except ValueError:
      print('Invalid input')
      continue
for i in range(1, num+1):
    if num % i == 0:
      print(f'{i} is a divisor of {num}')
time.sleep(5)
