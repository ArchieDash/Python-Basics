import csv
import time


def enrollment_stats(index):
    with open ('files/enrollments.csv', 'r') as file:
        data = csv.reader(file)
        return [int((row[index]).strip()) for row in data]


def main():
    enrolled = enrollment_stats(1)
    tuition = enrollment_stats(2)
    print(f'Total students: {sum(enrolled)}')
    print(f'Total tuition: $ {sum(tuition)}')
    print(f'\nStudent mean: {int(sum(enrolled)/len(enrolled))}')
    print(f'Student median: {max(enrolled)}')
    print(f'\nTuition mean: $ {int(sum(tuition)/len(tuition))}')
    print(f'Tuition median: $ {max(tuition)}')
    time.sleep(5)


main()
