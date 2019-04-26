"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

called_codes = []


def is_a_bangalore_num(num):
    '''
    :param num: input phone number (str)
    :return: True if input phone number belongs to someone in Bangalore else False (Bool)
    '''
    return num[1:4] == "080" and num[0] == "("


def is_num_mobile(num):
    '''
    :param num: input phone number (str)
    :return: True if input phone number is a mobile else False (Bool)
    '''
    return len(num) == 11 and num[5] == " "


def is_num_fixed(num):
    '''
    :param num: input phone number (str)
    :return: True if input phone number is a fixed line else False (Bool)
    '''
    return num[0] == "("


def get_mobile_prefix(num):
    '''
    :param num: input phone number (str)
    :return: 4-digit mobile prefix (str)
    '''
    return num[:4]


def get_fix_areacode(num):
    '''
    :param num: input phone number (str)
    :return: variable length area code for the fixed line (str)
    '''
    code_end = num.find(")")
    if code_end == -1:  # Defensive programming
        print(f"Unknown number type found: {num}")

    return num[1:code_end]


def is_num_telemarketer(num):
    '''
    :param num: input phone number (str)
    :return: True if input phone number is a telemarketer else False (Bool)
    '''
    # return num[5] != " " and num[0] != "(" --- Works but erroneous numbers may exist!

    if num[5] != " " and num[0] != "(":
        if num[:4] != "140":  # Defensive programming
            print(f"Unknown number type found:{num}")
        else:
            return True
    return False


from_bng_calls = 0  # Number of calls originating FROM Bangalore
to_bng_calls = 0  # Number of calls originating TO Bangalore FROM Bangalore
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c in calls:
        if is_a_bangalore_num(c[0]):
            from_bng_calls += 1
            if is_num_mobile(c[1]):
                called_codes.append(get_mobile_prefix(c[1]))
            elif is_num_fixed(c[1]):
                if is_a_bangalore_num(c[1]):
                    to_bng_calls += 1
                called_codes.append(get_fix_areacode(c[1]))
            elif is_num_telemarketer(c[1]):
                called_codes.append("140")
            else:
                print(f"Unknown number:{c[1]} found in data!")

called_codes = list(set(called_codes))

called_codes.sort()  # Python's sort arranges in increasing lexicographic order
print("The numbers called by people in Bangalore have codes:")
for cc in called_codes:
    print(cc)

print(f"{to_bng_calls*100/from_bng_calls:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed "
      f"lines in Bangalore.")


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
