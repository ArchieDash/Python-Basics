"""Returns the average number of N or 10K trials of random int at the certain range"""
import time
import random


def roll(a, b):
  return random.randint(a,b)


def main():
  a = int(input('Enter the start value: '))
  b = int(input('Enter the end value: '))
  num_of_trials = int(input('Enter the number of trials (defalt is 10.000): ') or 10000)
  trials =[roll(a, b) for trial in range(num_of_trials)]
  print(f'Average integer of {num_of_trials} trials is: {(sum(trials)/len(trials)):,.2f}')
  time.sleep(3)


main()
