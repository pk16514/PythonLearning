"""
   1. The syntax of the find() method is: str.find(sub[, start[, end]])

   2. The find() method takes maximum of three parameters:
      --> sub - It is the substring to be searched in the str string.

      --> start and end (optional)-
          The range str[start:end] within which substring is searched.

   3. The find() method returns an integer value:

      --> If the substring exists inside the string, it returns the index
          of the first occurence of the substring.

      --> If substring doesn't exist inside the string, it returns -1.
"""

# Example-1


quote1 = 'Let it be, let it be, let it be'

result1 = quote1.find('let it')
print("Substring 'let it':", result1)

result2 = quote1.find('small')
print("Substring 'small ':", result2)

if (quote1.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

# Example-2


quote2 = 'Do small things with great love'

print(quote2.find('small things', 10))
print(quote2.find('small things', 2))
print(quote2.find('o small ', 10, -1))
print(quote2.find('things ', 6, 20))
