"""Simple REPL"""
while True:
    prompt = input("(Type 'Q' to quit) >> ")
    if prompt.strip().lower() == 'q':
        break
