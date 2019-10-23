import time


def delayed_print(string):
    print(string)
    time.sleep(2)
    

def main():
    desserts = ['ice cream', 'cookies']
    desserts.sort()
    delayed_print(f'Sorted list with alphabedical order: {desserts}')
    delayed_print(f'The index of ice cream item is: {desserts.index("ice cream")}')
    food = desserts[:]
    food.extend(['broccoli','turnips'])
    delayed_print(f'{food} - food list\n{desserts} - desserts list')
    food.remove('cookies')
    delayed_print(f'{food[:2]} - first two items of the food list (cookies are deleted)')
    breakfast = 'cookies, cookies, cookies'.split(', ')
    delayed_print(f'{breakfast} - list from splited string')
    numbers = [2, 4, 8, 16, 32, 64]
    delayed_print(f'{numbers} - some bunch of numbers')
    for number in numbers:
        if number in range(1, 20):
            print(number)
    time.sleep(3)


main()
