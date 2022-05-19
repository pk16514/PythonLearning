vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()

vowels = list(vowels)

count = 0
dict = {}
for char in vowels:
    count = 0
    for j in range(len(ip_str)):
        if char == ip_str[j]:
            count += 1
    # dict[char] = count
    # dict.update({char: count})
    dict.setdefault(char, count)

print(dict)
print(dict.get('a', count))

# Method-2

count = {}.fromkeys(vowels, 0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)

# Method-3

count = {char: sum([1 for item in ip_str if item == char]) for char in vowels}

print(count)
