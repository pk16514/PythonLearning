"""
   1. The syntax of fromkeys() method is:
        dictionary.fromkeys(sequence[, value])

   2. fromkeys() method takes two parameters:
      --> sequence- sequence of elements which is to be used as
                    keys for the new dictionary

      --> value(Optional)- value which is set to each each element
                           of the dictionary

   3. fromkeys() method returns a new dictionary with the given sequence
      of elements as the keys of the dictionary.

      Note- If the value argument is set, each element of the newly created
            dictionary is set to the provided value.
"""
# Example-1


keys = {'a', 'e', 'i', 'o', 'u'}

vowels = dict.fromkeys(keys)
print(vowels)
print('\r')

# Example-2


keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
print('\r')

# Example-3

keys = {'aeiou'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
print('\r')

# Example-4(When the value is a mutable object)


seq = {'a', 'b', 'c', 'd', 'e'}
lis1 = [2, 3]

# using conventional method
res_dict = dict.fromkeys(seq, lis1)

print("The newly created dict with list values : " + str(res_dict))
lis1.append(4)

print("The dict with list values after appending : " + str(res_dict))

lis1 = [2, 3]
print('\n')

# list() func. returns another copied value doesn't modify the original.
# Does not reference to original iterator.

res_dict2 = {key: list(lis1) for key in seq}

print("The newly created dict with list values : " + str(res_dict2))

lis1.append(4)

print("The dict with list values after appending (no change) : " + str(res_dict2))
