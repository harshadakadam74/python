for i in range(12):
    print("5 X", i+1, "=" , 5 * (i+1))
    if (i == 10):
     break
 
 
for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=" , 5 * i)
    

# do-while example
i = 0
while True:
    print(i)
    i = i + 1
    if(i % 100 == 0):
        break
    
    
    
# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

# example
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

# example
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)
    
 
 