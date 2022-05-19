data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
wspos = data.find(' ', atpos)

email = data[(atpos + 1):wspos]
print(email)
