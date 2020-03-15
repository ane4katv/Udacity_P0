"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

count = 0
unique_nums = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for i in texts:
        if i[0] not in unique_nums:
            unique_nums.append(i[0])
            count+=1
        if i[1] not in unique_nums:
            unique_nums.append(i[1])
            count+=1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for i in calls:
        if i[0] not in unique_nums:
            unique_nums.append(i[0])
            count+=1
        if i[1] not in unique_nums:
            unique_nums.append(i[1])
            count+=1

print(f"There are {count} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
