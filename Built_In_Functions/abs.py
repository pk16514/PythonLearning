"""
   1. The syntax of abs() method is: abs(num)

   2. abs() method takes a single argument:
      --> num - a number whose absolute value is to be returned.
          The number can be:
                (1) integer
                (2) floating number
                (3) complex number

   3. abs() method returns the absolute value of the given number.
      --> For integers - integer absolute value is returned

      --> For floating numbers - floating absolute value is returned

      --> For complex numbers - magnitude of the number is returned
"""
# Example-1


integer = -20
print('Absolute value of -20 is:', abs(integer))

floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))

complex = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex))
