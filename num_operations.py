import time


print('Task_1')
while True:
    num = input('Enter an integer: ')
    try:
        num = int(num)
        print('Receiving the integer value is confirmed.')
        print(f'The product of your number and 3 equals: {num*3}')
        break
    except ValueError:
        print('Entered value is not an integer')
        continue
time.sleep(3)


print('\nTask_2')
while True:
    num = input('Enter an integer or float: ').replace(',','.')
    try:
        num = float(num)
        print('Receiving the float value is confirmed.')
        # leave as much decimal places as it was in input number
        print(f'The product of your number and 3 equals: {round(num, len(str(num))-1)*3}')
        break
    except ValueError:
        print('Entered value is not an integer or float')
        continue
time.sleep(3)


print('\nTask_3')
string = 'Snake'
num = 235
print(f'Interpolation of string "{string}" and integer "{str(num)}"')
time.sleep(3)


print('\nTask_4')
while True:
    nums = [input('Enter an integer: ') for num in range(2)]
    try:
        for n in [int(num) for num in nums]:
            result = int(nums[0]) * int(nums[1])
        print(f'The power of your numbers is equal: {result}')
        break
    except ValueError:
        print('Invalid input')
        continue
