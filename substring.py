import time


print('Task_1')
string = 'AAA'
print(f'Result: {string.find("a")}')
time.sleep(3)

print('\nTask_2')
string = 'version 2.0'
version = 2.0
print(f'Result: {string.find(str(version))}')
time.sleep(3)

print('\nTask_3')
string = input('STDIN: ')
match = input('Search the letter in StdIn: ')
while len(match.strip()) > 1:
    match = input('Input a letter:')
print(f'Result: {string.find(match)}')
time.sleep(3)
