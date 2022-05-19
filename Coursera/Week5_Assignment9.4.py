"""
Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.
"""

name = input("Enter file:")
handle = open(name)

count = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    char = line.split()
    email = char[1]

    count[email] = count.get(email, 0) + 1

Bigcount = -1

for committer, count in count.items():
    if count > Bigcount:
        Bigcount = count
        Bigcommitter = committer

print(Bigcommitter, Bigcount)
