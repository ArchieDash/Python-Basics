import time


while True:
    nums = input('Enter integers separate by space: ').strip().split()
    try:
        nums = [int(num) for num in nums] 
        print (f'The sum of integers equals: {sum(nums)}')
        break
    except ValueError:
        print('Invalid input format')
        continue
time.sleep(3)
