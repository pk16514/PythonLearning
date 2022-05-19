"""
   1. The syntax of filter() method is: filter(function, iterable)

   2. filter() method takes two parameters:
      --> function-
          function that tests if elements of an iterable return true or false

          If None, the function defaults to Identity function- which returns
          false if any elements are false

      --> iterable - iterable which is to be filtered, could be sets, lists,
                     tuples, or containers of any iterators

   3. filter() method returns an iterator that passed the function check for
      each element in the iterable.

   4. filter() method is equivalent to:
      --> when function is defined
          (element for element in iterable if function(element))

      --> when function is None
          (element for element in iterable if element)
"""
# Example-1


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False


filtered_vowels = list(filter(filter_vowels, letters))

print(filtered_vowels)
print('\r')

# Example-2


random_list = [1, 'a', 0, False, True, '0']

filtered_list = filter(None, random_list)

print('The filtered elements are:')
for element in filtered_list:
    print(element)
