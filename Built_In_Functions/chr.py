"""
   1. The syntax of chr() is: chr(i)

   2. chr() method takes a single parameter, an integer i.

      Note- The valid range of the integer is from 0 through 1,114,111.

   3. chr() returns a character(a string) whose Unicode code point
      is the integer i.

      Note- If the integer i is outside the range, ValueError will be raised.
"""
# Example-1


print(chr(97))
print(chr(65))
print(chr(1200))

# Example-2


print(chr(-1))
