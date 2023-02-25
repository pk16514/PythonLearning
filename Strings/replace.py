"""
   1. The syntax of replace() is: str.replace(old, new [, count])

   2. The replace() method can take maximum of 3 parameters:
      --> old- old substring you want to replace

      --> new- new substring which will replace the old substring

      --> count(optional)-
          the number of times you want to replace the old substring with the
           new substring

   3. The replace() method returns a copy of the string where the old
      substring is replaced with the new substring. The original string is
      unchanged. If the old substring is not found, it returns the copy of the
      original string

   4. If count is not specified, the replace() method replaces all occurrences
      of the old substring with the new substring.
"""
# Example-1


song1 = 'cold, cold heart'
print(song1.replace(' ', 'hurt', 1))

song2 = 'Let it be, let it be, let it be, let it be'
print(song2.replace('let', "don't let", 2))
print('\r')

# Example-2


song3 = 'cold, cold heart'
replaced_song3 = song3.replace('o', 'e')

print('Original string:', song3)
print('Replaced string:', replaced_song3)

song4 = 'let it be, let it be, let it be'
print(song4.replace('let', 'so', 0))
