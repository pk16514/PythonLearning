"""
   1. The syntax of divmod() is: divmod(x, y)

   2. divmod() takes two parameters:
      --> x - a non-complex number (numerator)

      --> y - a non-complex number (denominator)

   3. divmod() returns
      --> (q, r)- a pair of numbers (a tuple) consisting of
                   quotient q and remainder r

      Note- 1. If x and y are integers, the return value from divmod()
               is same as (a // b, x % y).

            2. If either x or y is a float, the result is (q, x%y).
               Here, q is the whole part of the quotient.
"""
# Example-1


print('divmod(8, 3) = ', divmod(8, 3))
print('divmod(3, 8) = ', divmod(3, 8))
print('divmod(5, 5) = ', divmod(5, 5))
print('\r')
# divmod() with Floats
print('divmod(8.0, 3) = ', divmod(8.0, 3))
print('divmod(3, 8.0) = ', divmod(3, 8.0))
print('divmod(7.5, 3) = ', divmod(7.5, 3))
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))
