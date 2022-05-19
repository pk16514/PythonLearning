fname = input('Enter the file name:- ')
fhand = open(fname, 'r')

count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

Frequentword = None
Bigcount = None
temp = []

for word, count in count.items():
    if Bigcount is None or count > Bigcount:
        Frequentword = word
        Bigcount = count
    temp.append((count, word))

# try using list comprehension also

temp.sort(reverse=True)

for count, word in temp[:10]:
    print(word, count)
