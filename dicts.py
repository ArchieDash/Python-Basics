import time
from collections import defaultdict


birthdays = defaultdict(lambda: "unknown", {"Luke Skywalker":"5/24/19",
                    "Obi-Wan Kenobi":"3/11/57", "Darth Vader":"4/1/41"}) #set the default value for any missed key to be 'unknown'
print(f"Yoda's birthday - {birthdays['Yoda']}\nDarth Vader's birthday - {birthdays['Darth Vader']}\n")
del birthdays["Darth Vader"] #delete position from the dict
for key, value in birthdays.items():
    if value != "unknown":
        print(f"{key} {value}") #print non-default key-value pairs
time.sleep(3)
