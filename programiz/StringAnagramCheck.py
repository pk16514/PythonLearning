"""
Two strings are said to be anagram if we can form one string by arranging
the characters of another string. For example, Race and Care. Here, we can
form Race by arranging the characters of Care.
"""

str1 = "Dusty"
str2 = "Study"

if len(str1) == len(str2):
    str1 = list(str1.lower())
    str1.sort()
    str2 = list(str2.lower())
    str2.sort()

    if(str1 == str2):
        print('Strings are anagram of each other')
    else:
        print('Strings are not anagram of each other')
else:
    print('Strings are not anagram of each other')
