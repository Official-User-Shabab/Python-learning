# Values are either True of False in python
# Any empty list, dictionary and the number 0 are False
# Otherwise everything else with some content is pretty much True

# This can be used in validation and checking stuff

age = 1

if age == 1:
  print(f"You are {age} years old") # These are f strings

# Nothing will be printed if the age was not 1

# To check whether something is of a data type, use function seen below:

x = 46
print(isinstance(x, int)) # Will be true

# Keywords for this function's data types are: int, str, bool, float, complex
