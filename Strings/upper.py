"""
   1. The syntax of upper() method is: string.upper()

   2. upper() method doesn't take any parameters.

   3. upper() method returns the uppercased string from the given string.
      It converts all lowercase characters to uppercase. If no lowercase
      characters exist, it returns the original string.
"""
# Example-1


string1 = "THIS SHOULD BE LOWERCASE!"
string2 = "Th!s Sh0uLd B3 L0w3rCas3!"

print(string1.upper())
print(string2.upper())

# Example-2


firstString = "PYTHON IS AWESOME!"
secondString = "PyThOn Is AwEsOmE!"

if(firstString.upper() == secondString.upper()):
    print("The strings are same.")
else:
    print("The strings are not same.")
