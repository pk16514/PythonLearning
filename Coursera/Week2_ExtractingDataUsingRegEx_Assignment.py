"""
The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
and summing up the integers.
"""

import re

fh = open('regex_sum_1217052.txt', 'r')
sum = 0
count = 0
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for number in x:
        number = int(number)
        sum += number
        count += 1

print(sum)
print(count)
