# int() - constructs an integer number from: an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from: an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from: a wide variety of data types, including strings, integer literals and float literals

age = input("How old are you?_") # The input from a user is always a string
int(age) # Hence it should be converted if needed

pi = 3.141 # This is a float
name = "dave" # Cannot be converted to anything else
