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