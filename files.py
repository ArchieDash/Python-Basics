import os
import time


path = os.path.join('files','poem.txt') #1st task
with open (path, 'r') as file:
    for line in file:
        print(line)
time.sleep(3)


output = os.path.join('files', 'poem(copy).txt') #2nd task
with open (path, 'r') as file, open (output, 'w') as copy:
    for line in file.readlines():
        copy.write(line)


with open (output, 'a') as file: #3th task
    file.write('\n\nPowered by INRI Labs.')
