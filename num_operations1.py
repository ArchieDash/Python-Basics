import time


print('Task_1')
while True:
    num = input('Enter a number: ')
    try:
        num = float(num)
        print(f'{num} rounded to 2 decimal places is {float(num):.2f}')
        break
    except ValueError:
        print('Invalid input')
        continue
time.sleep(3)

print('\nTask_2')
while True:
    num = input('Enter a number: ')
    try:
        num = float(num)
        print(f'The absolute value of {num} is {abs(num)}')
        break
    except ValueError:
        print('Invalid input')
        continue
time.sleep(3)

print('\nTask_3')
while True:
    num1 = input('Enter a number: ')
    num2 = input('Enter another number: ')
    try:
        num1 = float(num1)
        num2 = float(num2)
        print(f'The difference between {num1} and {num2} is an integer? {(num1-num2).is_integer() }!')
        break
    except ValueError:
        print('Invalid input')
        continue
time.sleep(3)
