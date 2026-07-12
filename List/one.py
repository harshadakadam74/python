marks = [1,2,3,4,5,6,7,8,9,"Heyy",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# negative index nikalne ki steps
print(marks[-3]) #negative index
print(marks[len(marks)-3]) #positive index
print (marks[11-3]) #positive index
print(marks[9]) #positive index 

if "Heyy" in marks:
    print("yes")
else:
    print("No")

# same thing applies for string as well!
if "He" in "Heyy":
    print("Yess")
    
print(marks[0:7])
print(marks[1:8])
print(marks[1:10:2])

animals = ["cat", "dog", "mouse", "horse", "bat", "goat", "cow"]
print(animals[4:]) # using positive index
print(animals[-4:]) #using negative index

animals = ["cat", "dog", "mouse", "horse", "bat", "goat", "cow"]
print(animals[:6]) # using positive index
print(animals[:-3]) #using negative index


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

names = ["John", "Aman", "kabir", "Rosa", "Anna"]
namesWith_0 = [item for item in names if "o" in item]
print(namesWith_0)

names = ["John", "Aman", "kabir", "Rosa", "Anna"]
namesWith_0 = [item for item in names if (len(item) > 4)]
print(namesWith_0)