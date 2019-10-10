while True:
    base = input('Enter a base: ')
    exponent = input('Enter an exponent: ')
    try:
        result = pow(float(base), float(exponent))
        print(f'{base.strip()} to the power of {exponent.strip()} = {result:.2f}')
        break
    except ValueError:
        print('Invalid input')
        continue
