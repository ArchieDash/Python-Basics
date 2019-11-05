import time


def convert_cel_to_far(celsius):
    return celsius * 9/5 + 32


def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    temperature = int(input('Enter a temperature in degrees F :'))
    print(f'{temperature} degrees F = {convert_far_to_cel(temperature):.2f} C')
    temperature = int(input('Enter a temperature in degrees C :'))
    print(f'{temperature} degrees C = {convert_cel_to_far(temperature):.2f} F')
    time.sleep(3)


main()
