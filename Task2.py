"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict
import csv

phone_time_dict = defaultdict(int)  # Contains keys as telephone numbers and value as time on phone
max_time_phone_num = ""
max_call_time = 0

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c in calls:
        phone_time_dict[c[0]] += int(c[3])  # Calling Time
        phone_time_dict[c[1]] += int(c[3])  # Answering Time

        # Implementation 1 - O(n) time complexity
        if max(phone_time_dict[c[0]], phone_time_dict[c[1]]) > max_call_time:
            max_time_phone_num, max_call_time = (c[0], phone_time_dict[c[0]]) if phone_time_dict[c[0]] > phone_time_dict[c[1]] else (c[1], phone_time_dict[c[1]])

        # Implementation 2 - O(n) time complexity
        # Alternate implementation - can write a function to avoid duplicate code
        # if phone_time_dict[c[0]] > max_call_time:
        #     max_time_phone_num = c[0]
        #     max_call_time = phone_time_dict[c[0]]
        #
        # if phone_time_dict[c[1]] > max_call_time:
        #     max_time_phone_num = c[1]
        #     max_call_time = phone_time_dict[c[1]]


# Implementation 3 - O(nlogn) time complexity
# Can sort the dict like phone_time_dict = sorted(phone_time_dict.items(),key= lambda x: x[1], reverse=True) and return the first value
# But time complexity would be O(nlogn) where n = len(phone_time_dict)
# phone_time_dict = sorted(phone_time_dict.items(),key= lambda x: x[1], reverse=True)
# print(phone_time_dict[0])

# Implementation 4 - O(n) time complexity but with higher constants
# Iterating for time complexity O(n)
# max_time_phone_num = ""
# max_call_time = 0
# for k,v in phone_time_dict.items():
#     if v > max_call_time:
#         max_time_phone_num = k
#         max_call_time = v

print(f"{max_time_phone_num} spent the longest time, {max_call_time} seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

