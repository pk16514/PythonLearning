"""
1. Python’s strings are in unicode, which allows for characters to be from a much larger
   alphabet, including more than 75,000 ideographic characters used in Chinese, Japanese,
   and Korean alphabets. Everything works fine inside Python, for operations like slicing
   and appending and concatenating strings and using .find() or the in operator.

2  Things only get tricky when you want to input strings into Python, or print them to an
   output window or write them to a file. For output, your terminal (output) window will
   typically be set up to display characters only from a restricted set of languages
   (perhaps just English). If you issue a print statement on a string containing other
   characters, it may not display correctly in your terminal window. Indeed, you may get an
   error message.

3. When there are 75,000 possible characters, they can’t all be encoded with a single byte,
   because there are only 256 distinct bytes (eight-bit sequences). There are many possible
   encodings. The one you will be most likely to encounter, using REST APIs, is called UTF-8.
   A single unicode character is mapped to a sequence of up to four bytes.

4. If you read in a UTF-8 encoded text, and get the contents using .read() or .readlines(),
   you will need to “decode” the contents in order to turn it into a proper unicode string
   that you can read and use.

5. Fortunately, the requests module will normally handle this for us automatically. When we
   fetch a webpage that is in json format, the webpage will have a header called ‘content-type’
   that will say something like application/json; charset=utf8. If it specifies the utf8
   character set in that way, the requests module will automatically decode the contents into
   unicode: requests.get('that web page').text will yield a string, with each of those sequences
   of one to four bytes coverted into a single character.

   If, for some reason, you get json-formatted text that is utf-encoded but the requests module
   hasn’t magically decoded it for you, the json.loads() function call can take care of the
   decoding for you. loads() takes an optional parameter, encoding. Its default value is ‘utf-8’,
   so you don’t need to specify it unless you think the text you have received was in some other
   encoding than ‘utf-8’.
"""

# Problem-1

"""
Q.> When you have non-ASCII characters in a string and you get an error trying to write them,
    which method should you invoke on the string?
A. ``.encode()``
B. ``.decode()``
C. ``.json()``
"""

# Problem-2

"""
Q.> In the textbook environment, what should you do if you are unable to write data to a file
    because of a Unicode encoding error?
A. Call ``.encode()``
B. Call ``.decode()``
C. Call ``.json()``
D. Get different data, because we don't have ``.encode()`` available in the Runestone environment.
"""
