import re
from pprint import pprint

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    all_code_list = []
    to_bangalore_list = []

    for i in calls:
        from_bangalore = re.findall(r'^\W080\W\d+$', i[0])
        all_codes = re.findall(r'\(?\d+\)?\s?\d+', i[1])
        to_bangalore = re.findall(r'^\W080\W\d+$', i[1])

        if from_bangalore and all_codes:
            all_code_list += all_codes

        # percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.
        if from_bangalore and to_bangalore:
            to_bangalore_list += to_bangalore

code_list = (sorted(list(set(all_code_list))))
percentage = round(100 * float(len(to_bangalore_list)) / float(len(all_code_list)), 2)

print("**** Part A ****")
print("The numbers called by people in Bangalore have codes: ")
print(*code_list, sep='\n')

print("\n**** Part B ****")
print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

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