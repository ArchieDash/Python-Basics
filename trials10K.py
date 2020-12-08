"""Returns the average number of N for 10K trials of random int at the certain range"""
import random
from collections import Counter
import matplotlib.pyplot as plt


def roll(a: int, b: int) -> int:
    return random.randint(a,b)


def main():
    a = int(input("Enter the start value: "))
    b = int(input("Enter the end value: "))
    num_of_trials = int(input("Enter the number of trials (defalt is 10.000): ") or 10_000)
    trials =[roll(a, b) for trial in range(num_of_trials)]
    print(f"Average integer of {num_of_trials} trials is: {(sum(trials)/len(trials)):,.2f}")
  
    plt.title(f"Results of {num_of_trials} random rolls  from range {a} : {b}")
    plt.xlabel("Integer")
    plt.ylabel("Trials")
    plt.bar(Counter(trials).keys(), Counter(trials).values())
    plt.show()
  
  
if __name__ == "__main__":
    main()
