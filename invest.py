import time


def invest(amount, rate, years):
    for year in range(years):
      amount += amount * (rate/100)
      print(f'year {year+1}: ${amount:.2f}')


def main():
    while True:
      try:
        amount = float(input('Amount for investment: '))
        rate = float(input('Rate of investment (%): '))
        years = int(input('Years of investment: '))
        break
      except ValueError:
        print('Invalid input')
        continue
    invest(amount, rate, years)
    time.sleep(3)


main()
