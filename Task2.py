"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from pprint import pprint

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

di = dict()
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


    for i in calls:
        di[i[0]] = di.get(i[0], 0) + int(i[3])
        di[i[1]] = di.get(i[1], 0) + int(i[3])

        all_numbers = [(value, key) for key, value in di.items()]
        longest_number = max(all_numbers)[1]
        duration = max(all_numbers)[0]


print(f"{longest_number} spent the longest time, {duration} seconds, on the phone during September 2016.")



"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

