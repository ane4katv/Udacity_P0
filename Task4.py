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

    outgoing = []
    receiving = []
    potential_telemarketers = []

for i in calls:
    receiving.append(i[1])
    if i[0] not in texts:
        outgoing.append(i[0])
for i in outgoing:
    if i not in receiving:
        potential_telemarketers.append(i)

potential_telemarketers = list(set(potential_telemarketers))
potential_telemarketers.sort()

print("These numbers could be telemarketers: ")
print(*potential_telemarketers, sep="\n")

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

