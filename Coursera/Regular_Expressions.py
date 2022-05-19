"""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
\b       Matches the empty string, but only at the start or end of a word.
\B       Matches the empty string, but not at the start or end of a word.
\d       Matches any decimal digit. Equivalent to [0-9]
\D       Matches any non-decimal digit. Equivalent to [^0-9]

1. re.search()
   The re.search() method takes two arguments: a pattern and a string. The method looks for the first
   location where the RegEx pattern produces a match with the string.
   If the search is successful, re.search() returns a match object; if not, it returns None.
   match = re.search(pattern, str)

2. re.findall()
   The re.findall() method returns a list of strings containing all matches. If the pattern is not found,
   re.findall() returns an empty list.

3. re.split()
   The re.split method splits the string where there is a match and returns a list of strings where
   the splits have occurred. If the pattern is not found, re.split() returns a list containing the
   original string.

4. re.sub()
   The method returns a string where matched occurrences are replaced with the content of replace variable.
   re.sub(pattern, replace, string)
   If the pattern is not found, re.sub() returns the original string.
   You can pass count as a fourth parameter to the re.sub() method. If omited, it results to 0.
   This will replace all occurrences.

5. re.subn()
   The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string
   and the number of substitutions made.
"""

import re

# find

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

print()

# startswith

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

print()

# re.search()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # if re.search('From:', line):
    if re.search('^From:', line):
        print(line)

print()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

print()

# re.findall()

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

print()

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)

print()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

print()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

print()
# re.split()

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)

print()

# re.sub()

string = 'abc 12\
de 23 \n f45 6'

pattern = '\s+'
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)

print()

# re.subn()

string = 'abc 12\
de 23 \n f45 6'

pattern = '\s+'
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)

# Escape character

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
