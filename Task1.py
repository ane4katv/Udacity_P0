"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

di = dict()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for i in texts:
        if i[0] in di:
            di[i[0]] += 1
        else:
            di[i[0]] = 1

        if i[1] in di:
            di[i[1]] += 1
        else:
            di[i[1]] = 1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for i in calls:
        if i[0] in di:
            di[i[0]] += 1
        else:
            di[i[0]] = 1

        if i[1] in di:
            di[i[1]] += 1
        else:
            di[i[1]] = 1

records_num = len(di)


print(f"There are {records_num} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
