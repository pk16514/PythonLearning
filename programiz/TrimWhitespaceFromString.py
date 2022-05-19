"""
Note- 1. strip() removes the leading and trailing characters including the
         whitespaces from a string.

      2. However, if you have characters in the string like '\n' and you want
         to remove only the whitespaces, you need to specify it explicitly on
         the strip() method as shown in the following code.
"""

# Example-1

my_string = " Python "

print(my_string.strip())

# Example-2

my_string = " \nPython "

print(my_string.strip(" "))
