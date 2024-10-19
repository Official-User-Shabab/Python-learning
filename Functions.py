# A function is always DEFINED first, like this:
def myfunction(num1, num2):
  print('''
  The paranthese or "()" include variables, now being called parameters
  These variables can now be used in the function
  The function is like a mini codebase within your code
  Use functions to make your code less repeated and more readable
  ''')
  return num1 + num2 # Returns this back to store in that variable "sum"


num1 = 4
num2 = 8
sum = myfunction(num1, num2) # These are arguments; variables being sent to or passed into a function

# Think of functions like machines, that can take "boxes" or variables as arguments, and process them
