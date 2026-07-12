num = 18
if(num < 0):
    print("The number is negative")
elif(num > 0):
    if(num <= 10):
        print("The number is between 1 to 10")
    elif(num > 10 and num <= 20):
        print("The number is between 11 to 20")
    else:
        print("The number is greater than 20")
else:
    print("The number is zero")
    
# Nested if statements
# We can use if, if-else, elif statements inside other if statements as well.
# Example:

# num = 18
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")
# Output:

# Number is between 11-20
    
#