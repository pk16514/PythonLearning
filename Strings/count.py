"""
   1. The syntax of count() method is: string.count(substring, start, end)

   2. count() method only requires a single parameter for execution. However,
      it also has two optional parameters:
      --> substring- string whose count is to be found

      --> start(Optional)- starting index within the string where search starts

      --> end(Optional)- ending index within the string where search ends

   3. count() method returns the number of occurrences of the substring in the
      given string.
"""
# Example-1


string = "Python is awesome, isn't it?"
substring1 = "is"
substring2 = "i"

count1 = string.count(substring1)
print("The count is:", count1)

count2 = string.count(substring2, 8, 25)
print("The count is:", count2)
