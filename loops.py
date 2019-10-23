import time


def double(n):
    return n*2


print('Task_1')
for num in range(2,11):
    print(num)
time.sleep(3)

print('\nTask_2')
num = 1
while num < 10:
    num += 1
    print(num)
time.sleep(3)

print('\nTask_3')
stdout = double(2)
for n in range(3):
    print(stdout)
    stdout = double(stdout)
