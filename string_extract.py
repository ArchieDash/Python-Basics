import time

print('Task_1')

strings = ['Animals', 'Banger', 'Honey Bee', 'Honeybadger']
for word in strings:
    print(word.lower())
time.sleep(3)


print('\nTask_2')
strings = ['Animals', 'Banger', 'Honey Bee', 'Honeybadger']
for word in strings:
    print(word.upper())
time.sleep(3)


print('\nTask_3')
strings = ['   Filet Mignon', 'Brisket   ', '  Cheeseburger  ']
for word in strings:
    print(word.strip())
time.sleep(3)


print('\nTask_4')
strings = ['Becomes', 'becomes', 'BEAR', ' bEautiful']
for word in strings:
    print(word.startswith('be'))
time.sleep(3)


print('\nTask_5')
for word in strings:
    print(word.strip().lower().startswith('be'))
time.sleep(10)
