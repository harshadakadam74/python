
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