# String are immutable in python. Once a string is created, it cannot be changed. However, we can create a new string based on the existing string.
a = "!!!Kadam!!!!! !!!!!!Kadam"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Kadam", "Harshada"))
print(a.split(" "))

blogHeading = "Python is a programming language that lets you work quickly and integrate systems more effectively."
print(blogHeading.capitalize())

str1 = "Python is a programming language that lets you work quickly!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Kadam"))

str1 = "Python is a programming language !!!"
print(str1.endswith("!!!"))

str1 = "Python is a programming language !!!"
print(str1.endswith("is",4,10))

str1 = "Python is a programming language !!!"
print(str1.find("a")) #ture
# print(str1.find("as")) #false
# print(str1.index("as")) #error

str1 = "PythonIsAProgrammingLanguage"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "Python is a programming\n"
print(str1)
print(str1.isprintable())
str1 = "       " #useing spacebar
print(str1.isspace())

str2 = "  "
print(str2.isspace()) # using tab

str1 = "Python Is A Programming"
print(str1.istitle())

str2 = "To kill a mockingbird"
print(str2.istitle())

str1 = "Python is a programming language that lets you work quickly and integrate systems more effectively."
print(str1.startswith("Python"))

str1 = "Python is a programming language that lets you work quickly and integrate systems more effectively."
print(str1.swapcase())

str1 = "Python is a programming language that lets you work quickly and integrate systems more effectively."
print(str1.title())