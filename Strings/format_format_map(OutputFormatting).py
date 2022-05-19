"""
   1. In case of float(f), after decimal max. no of digits can be 6.

   2. In case of Number formatting with signed numbers-
      --> for {+f}, in case of positive no show the +ve sign
                    in case of negative no show as it is.

      --> for {-f}, in case of positive no show as it is
                    in case of negative no show the -ve sign

      --> for { f}, in case of positive no show the whitespace
                    in case of negative no show as it is

   3. In case of Number formatting with alignment-
      --> '=' sign Forces the signed (+) (-) to the leftmost position

   4. Python internally uses getattr() for class members in the form ".age".
      And, it uses __getitem__() lookup for dictionary members in the form
      "[index]".
"""
# Formatting output using String modulo operator(%):


print("Geeks : %02d, Portal : %5.4f" % (1, 5.333))
print("Total students : %3d, Boys : %4d" % (240, 120))
print("%7.3o" % (25))
print("%9.3E" % (356.08977))
print('\r')

# Formatting output using the format method:
# Example-1: Basic formatting for default, positional and keyword arguments


print("Hello {}, your balance is {}.".format("Adam", 230.2346))
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
print('\r')

# Example-2: Simple number formatting


print("The number is:{:d}".format(123))
print("The float number is:{:f}".format(123.4567898))
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
print('\r')

# Example-3: Number formatting with padding for int and floats


print("{:5d}".format(12))
print("{:2d}".format(1234))
print("{:8.3f}".format(12.2346))
print("{:05d}".format(12))
print("{:08.3f}".format(12.2346))
print('\r')

# Example-4: Number formatting for signed numbers


print("{:+f} {:+f}".format(12.23, -12.23))
print("{:-f} {:-f}".format(12.23, -12.23))
print("{: f} {: f}".format(12.23, -12.23))
print('\r')

# Example-5: Number formatting with left, right and center alignment


print("{:5d}".format(12))
print("{:^10.3f}".format(12.2346))
print("{:<05d}".format(12))
print("{:=8.3f}".format(+12.2346))
print("{:=8.3f}".format(-12.2346))
print('\r')

# Example-6: String formatting with padding and alignment

# string padding with left alignment
print("{:5}".format("cat"))
print("{:>5}".format("cat"))
print("{:^5}".format("cat"))
print("{:*^5}".format("cat"))
print('\r')

# Example-7: Truncating strings with format()


print("{:.3}".format("caterpillar"))
# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))
print("{:^5.3}".format("caterpillar"))
print('\r')

# Example-8: Formatting class members using format()


class Person:
    age = 23
    name = "Adam"


print("{p.name}'s age is: {p.age}".format(p=Person()))
print('\r')

# Example-9: Formatting dictionary members using format()


person = {'age': 23, 'name': 'Adam'}

print("{p[name]}'s age is: {p[age]}".format(p=person))
print('\r')

# Example-10: Dynamic formatting using format()


string = "{:{fill}{align}{width}}"
print(string.format('cat', fill='*', align='^', width=5))

num = "{:{align}{width}.{precision}f}"
print(num.format(123.236, align='<', width=8, precision=2))
print('\r')

# Formatting dictionary members using format(**mapping):


person = {'age': 23, 'name': 'Adam'}

print("{name}'s age is: {age}".format(**person))
print('\r')
