"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_telephone_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for t in texts:
        unique_telephone_numbers.add(t[0])
        unique_telephone_numbers.add(t[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c in calls:
        unique_telephone_numbers.add(c[0])
        unique_telephone_numbers.add(c[1])

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
