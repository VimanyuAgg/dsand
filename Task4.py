"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

outgoing_call_nums = set()
incoming_call_nums = set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c in calls:
        outgoing_call_nums.add(c[0])
        incoming_call_nums.add(c[1])

# Filter outgoing callers based on incoming call records
possible_telemarketers = outgoing_call_nums - incoming_call_nums  # Set subtraction

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for t in texts:
        if t[0] in possible_telemarketers:  # O(1) operation
            possible_telemarketers.remove(t[0])

        if t[1] in possible_telemarketers:  # O(1) operation
            possible_telemarketers.remove(t[1])

possible_telemarketers = list(possible_telemarketers)
possible_telemarketers.sort()
print("These numbers could be telemarketers: ")

for tel in possible_telemarketers:
    print(tel)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

