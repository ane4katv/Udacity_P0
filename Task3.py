import re

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.

COMMENT:
Great effort but there is a simple misunderstanding.

First, we have to check whether caller or calls[0] is having the Bangalore area code i.e. (080) or not.
If yes, then we have to fetch the area code of the receiver's number i.e calls[1].
The receiver's number is divided into 3 parts

Fixed-line number - enclosed in brackets. You can use find() to fetch the index of the closing bracket.
Mobile number - starts with 7, 8, 9 and it's starting 4 digits.
Telemarketers number - starts with area code 140.
Once you fetch all the area code we have to sort and display them.

"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    all_codes_list = []
    from_bangalore_count = 0
    to_bangalore_count = 0

    for i in calls:

        if i[0][0:5] == "(080)":
            if i[1][0] == "(":
                fixed = i[1][i[1].find("(") + 1: i[1].find(")")]
                all_codes_list.append(fixed)
            if i[1][0] == "7" or i[1][0] == "8" or i[1][0] == "9":
                mobile = i[1][0:4]
                all_codes_list.append(mobile)
            if i[1][0:3] == "140":
                telemarketers = i[1][0:3]
                all_codes_list.append(telemarketers)

        # percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.
            from_bangalore_count += 1
            if i[1][0:5] == "(080)":
                to_bangalore_count += 1

    result = []
    for code in all_codes_list:
        if code not in result:
            result.append(code)
    result.sort()

    percentage = round(100 * float(to_bangalore_count) / float(from_bangalore_count), 2)

print("**** Part A ****")
print("The numbers called by people in Bangalore have codes: ")
print(*result, sep="\n")

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