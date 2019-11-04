import time


print('Task_1')
weight = 0.2
animal = 'newt'
#stdout using only string concatenation
print(str(weight) + ' kg is the weight of the ' + animal + '.')
time.sleep(3)

print('\nTask_2')
#stdout using format method
print('{} kg is the weight of the {}.'.format(weight, animal))
time.sleep(3)

print('\nTask_3')
#stdout using f-string
print(f'{weight} kg is the weight of the {animal}.')
time.sleep(3)
