"""
   1. The syntax of open() is:
        open(file, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None, closefd=True, opener=None)

   2. open() Parameters:
      --> file- path-like object(representing a file system path)

      --> mode(optional)-
          mode while opening a file. If not provided, it defaults to 'r'
          (open for reading in text mode). Available file modes are:
          (1) 'r'- Open a file for reading. (default)

          (2) 'w'- Open a file for writing. Creates a new file if it
                   does not exist or truncates the file if it exists.

          (3) 'x'- Open a file for exclusive creation. If the file already
                   exists, the operation fails.

          (4) 'a'- Open for appending at the end of the file without truncating
                   it. Creates a new file if it does not exist.

          (5) 't'- Open in text mode. (default)

          (6) 'b'- Open in binary mode.

          (7) '+'- Open a file for updating (reading and writing)

      --> buffering(optional)- used for setting buffering policy

      --> encoding(optional)- the encoding format

      --> errors(optional)-
          string specifying how to handle encoding/decoding error

      --> newline​(optional)-
          how newlines mode works(ex: None, ' ', '\n', 'r', and '\r\n')

      --> closefd(optional)- must be True (default); if given otherwise,
                             an exception will be raised

      --> opener(optional)- a custom opener; must return an open file
                            descriptor

   3. The open() function returns a file object which can used to read,
      write and modify the file.

      Note- If the file is not found, it raises the FileNotFoundError
            exception.

   4. Default encoding is platform dependent. In windows, it is 'cp1252'
      but 'utf-8' in linux. Hence, when working with files in text mode,
      it is highly recommended to specify the encoding type.
"""
# Example-1


f = open("PK.txt")
f = open("/home/prabhakar/Downloads/mbox-short.txt")

# Example-2


f = open("mbox.txt", mode='r')
f = open("mbox.txt", mode='w')
f = open("mbox.txt", mode='a')
f = open("mbox.txt", mode='r', encoding='utf-8')
