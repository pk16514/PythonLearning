"""
1. Encoding : The encode() function is used to convert the python object into a JSON string representation.
              It is also known as Serialization.

2. Decoding: The decode() function is used to convert the JSON object into python-format type.
             It is also known as DeSerialization.

3. json.load method-
   json.load() takes a file object and returns the json object. It is used to read JSON encoded data
   from a file and convert it into a Python dictionary and deserialize a file itself i.e. it accepts
   a file object.

   Syntax: json.load(fp)
   Parameters:
           fp: File pointer to read text.

4. json.loads method-
   json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
   It is mainly used for deserializing native string, byte, or byte array which consists of JSON data
   into Python Dictionary.

   Syntax: json.loads(s)
   Parameters:
           s: Deserialize str (s) instance containing a JSON document to a Python object using this
              conversion table.

5 json.dump method-
  json.dump() method can be used for writing to JSON file.

  Syntax: json.dump(dict, file_pointer)

  Parameters:
          dictionary – name of dictionary which should be converted to JSON object.
          file pointer – pointer of the file opened in write or append mode.

6. json.dumps method-
   json.dumps() method can convert a Python object into a JSON string.

   Syntax: json.dumps(dict, indent)

   Parameters:
           dictionary – name of dictionary which should be converted to JSON object.
           indent – defines the number of units for indentation

7. The .json() method is not defined for strings. Whenever we make a request to a specified URI through
   Python, it returns a response object. It is one of the most used methods in requests module.
"""
