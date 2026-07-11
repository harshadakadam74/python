# def average(a=9, b=8):
    # print("The average is ",(a+b/2))
    
# average(4,6)
# average(b=9)

# Defuilt arguments
def name(fname, mname = "john", lname = "rohit"):
    print("Hello,",fname,mname,lname)
name("Amy","Agarwal")

# Keyword arhuments
def name(fname, mname, lname):
    print("Hello,",fname,mname,lname)
name(mname = "peter", lname = "Master", fname = "john")

# Required arguments
'''def name(fname, mname, lname):
    print("Hello,",fname,mname,lname)
name("Peter","Quill")'''
# Define the error missing 1 required position 

def name(fname, mname, lname):
    print("Hello,",fname,mname,lname)
name("Peter","Ego","Quill")

# Arbitrary arguments
def name(*name):
    print("Hello,",name[0],name[1],name[2])
name("Peters","Egos","Quills")


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ",sum/len(numbers))
    
average(5,6,7,1)


def name(**name):
    print("Hello,",name["fname"], name["mname"], name["lname"])
name(mname = "xyz", lname = "john", fname = "kabir")


# return statemant
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
    
c = average(5,6,7,1)
print(c)


