"""Check the lenght of the input string with boolean comparison"""
string = input("Type some string: ")
if len(string) > 5:
    print("Length of the string is greater than 5 chars.")
elif len(string) < 5:
    print("Length of the string is less than 5 chars.")
else:
    print("Length of the string is equal to 5 chars.")
