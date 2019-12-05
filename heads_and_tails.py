'''Returns the average length of sequence of flipping coin to get both heads and tails'''
import time
import random
import PyPDF2
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin():
    flip = random.randint(0,1)
    if flip == 0:
      return 'heads'
    else:
      return 'tails'


def sequence_generator():
    sequence = [flip_coin() for n in range(2)]
    if sequence[0] != sequence[1]:
      return sequence
    else:
      while True:
        sequence.append(flip_coin())
        if sequence[-1] != sequence[-2]:
          return sequence


def main():
    num_of_trials = int(input('Number of trials:') or 10_000)
    trials = [len(sequence_generator()) for trial in range(num_of_trials)]
    results = Counter(trials)
    print(results)
    print(f'Average lenght of sequence is: {(sum(trials)/len(trials)):.2f}')
    # TODO: aggregate the graph (bars) of the stats
    plt.bar(results.keys(), results.values())
    plt.xlabel("Lenght of the sequence")
    plt.ylabel("Trials count")
    plt.savefig("Heads&Tails.png")
    plt.show()
    # TODO: save data (as table, grapth) to PDF report template
    time.sleep(3)


if __name__ == '__main__':
  main()
