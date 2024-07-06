# Strings are for words, letters, and some other stuff too

name = "vincent"
occupation = 'doctor' # Both " and ' are same

greetingLine = "Welcome Mr 'Vincent'" # Using a different type of string inside the outer one makes it appear/stand out

speech = """
This is part of a long
speech inside
a multiline string
where ' can be used
instead of " too
"""

username = "Vincie"
print(name[0]) # They can be used like arrays, split to letters

for x in "watermelons":
  print(x)
  # And so can be looped through too

# len(variable) gives the length of a variable

# SLICING THE STRING
slicendice = "Splity splicy"
print(slicendice[2:5])

# assume var = some string
# var.upper() or var.lower() turns all letters to uppercase and lowercase respectively
# var.strip() takes out/removes the spaces at the beginning or ending of strings
# var.replace(a, e) <- replaces all the a's in a string with e
# you can add strings too! (concatenation) Just add variables with strings and store that in a new variable (don't have to)

age = 45
text = f"My name is Bond, and I am {age}" # Formatted strings

# A good chart when strings concatenation and formatting starts getting difficult:

# \'	= Single Quote
# \\	= Backslash	
# \n	= New Line	
# \r	= Carriage Return	
# \t	= Tab	
# \b	= Backspace	
# \f	= Form Feed	
# \ooo	= Octal value	
# \xhh	= Hex value


# This is all the methods (like var.upper()) that you can use with strings:

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
