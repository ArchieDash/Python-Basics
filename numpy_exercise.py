import time
import numpy as np


first_matrix = np.arange(3, 12).reshape(3, 3)
print('First matrix:\n', first_matrix)
time.sleep(3)
print('\nMin of the first matrix:', np.min(first_matrix))
print(f'Max of the first matrix: {np.max(first_matrix)}')
print(f'Mean of the first matrix: {np.mean(first_matrix)}')
time.sleep(3)

second_matrix = first_matrix**2
print('\nSecond matrix:\n', second_matrix)
time.sleep(3)

third_matrix = np.vstack([first_matrix, second_matrix])
print('\nVertical stack of the first and second matrices:\n', third_matrix)
time.sleep(3)

product = third_matrix @ first_matrix
print('\nThe product of the third and first matrices:\n' , product)
time.sleep(3)

print('\nReshape of the third matrix:\n', third_matrix.reshape(3, 3, 2))
time.sleep(3)
