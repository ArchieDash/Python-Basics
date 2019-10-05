import random
import time

scores = 0
capitals = {"Alabama": "Montgomery",
            "Alaska": "Juneau",
            "Arizona": "Phoenix",
            "Arkansas": "Little Rock",
            "California": "Sacramento",
            "Colorado": "Denver", 
            "Connecticut": "Hartford",
            "Delawer": "Dover",
            "Florida": "Tallahassee",
            "Georgia": "Atlanta"}

while True:
    question = random.choice(list(capitals.keys()))
    answer = input(f'Capital of the {question} is: ')
    if answer.strip().capitalize() == capitals[question]:
        print('Correct!')
        scores +=1
        continue
    elif answer.strip().lower() == 'exit':
        print(f'Goodbye! You have answered correctly {scores} times!')
        print(f'The correct answer for the last guess was: {capitals[question]}')
        time.sleep(5)
        break
    else:
        print('That was not quite true. Try again.')
        continue
