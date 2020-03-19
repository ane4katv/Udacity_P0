"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
COMMENT:
The telemarketer's numbers are not correctly calculated.

Note:

1. We can iterate over the call list and store call[0] into an outgoing set and call[1] into a non_tele set
2. Similarly, iterate over the text list and store text[0] and text[1] into a non_tele set
3. To get the result we can subtract outgoing set to non_tele set.
4. Display in sorted order.

"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    outgoing = []
    not_telemarketers = []
    potential_telemarketers = []
    result = []

for i in calls:
    outgoing.append(i[0])
    not_telemarketers.append(i[1])

for i in texts:
    not_telemarketers.append(i[0])
    not_telemarketers.append(i[1])

for i in outgoing:
    if i not in not_telemarketers:
        potential_telemarketers.append(i)

potential_telemarketers = list(set(potential_telemarketers))
for i in potential_telemarketers:
    if i not in result:
        result.append(i)

result.sort()

print("These numbers could be telemarketers: ")
print(*result, sep="\n")

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

