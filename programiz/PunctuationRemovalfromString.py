punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# Method-1

for i in my_str:
    if i in punctuations:
        new_str = my_str.replace(i, "")
        my_str = new_str
    else:
        pass

print(my_str)

# Method-2

new_char = ""
for char in my_str:
    if char not in punctuations:
        new_char = new_char + char

print(new_char)
