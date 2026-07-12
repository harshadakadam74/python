
# Use this menthod in function
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greator")
    else:
        print("Second number is greator")
a = 9
b = 12
calculateGmean(a,b)
isGreater(a,b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)

c = 8
d = 7
calculateGmean(c,d)
isGreater(c,d)
# gmean2 = (a*b)/(a+b)
# print(gmean2)



# Build in function
numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
print("Type:", type(numbers))


'''Python has 70+ built-in functions, including print(), 
input(), len(), range(), type(), sum(), max(), min(), sorted(),
abs(), round(), zip(), map(), filter(), open(), eval(), 
isinstance(), id(), dir(), and many more.'''



# Python Functions
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# Built-in functions
# User-defined functions
# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# Syntax:
# def function_name(parameters):
#   pass
#   # Code and Statements
# Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
# Any parameters and arguments should be placed within the parentheses.
# Rules to naming function are similar to that of naming variables.
# Any statements and other code within the function should be indented.
# Calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

# Example:

# def name(fname, lname):
#     print("Hello,", fname, lname)

# name("Sam", "Wilson")
# Output:

# Hello, Sam Wilson