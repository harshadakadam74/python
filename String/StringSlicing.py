fruit = "Mango"
mongoLen = len(fruit)
print(mongoLen)
print(fruit[0:4]) #including 0 but not 4
print(fruit[1:4]) #including 1 but not 4
print(fruit[:5]) #including 0 but not 5
print(fruit[0:-3]) #including 0 but not -3
print(fruit[len(fruit)-3]) #including the character at index (length - 3)
print(fruit[-1:len(fruit)-3]) #including -1 but not (length - 3)
print(fruit[-3:-1]) #including -3 but not -1

pr = "Harry"
print(pr[-4:-2])