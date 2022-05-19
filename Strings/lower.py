"""
   1. The syntax of lower() method is: string.lower()

   2. lower() method doesn't take any parameters.

   3. lower() method returns the lowercased string from the given string.
      It converts all uppercase characters to lowercase. If no uppercase
      characters exist, it returns the original string.
"""
# Example-1


string1 = "THIS SHOULD BE LOWERCASE!"
string2 = "Th!s Sh0uLd B3 L0w3rCas3!"

print(string1.lower())
print(string2.lower())

# Example-2


firstString = "PYTHON IS AWESOME!"
secondString = "PyThOn Is AwEsOmE!"

if(firstString.lower() == secondString.lower()):
    print("The strings are same.")
else:
    print("The strings are not same.")
