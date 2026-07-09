import time
name = input("Enter your name:")
Time =  time.strftime("%H:%M:%S")
presentTime = int(time.strftime("%H"))
if (4 <= presentTime <= 12 ):
    print("Good Morning",name ,"It's time:",presentTime) 
elif (12 >= presentTime <= 5 ):
    print("Good Afternoon",name ,"It's time:",presentTime)
elif (5 >= presentTime <= 8 ):
    print("Good Evening",name ,"It's time:",presentTime)
else:
    print("Good Night",name ,"It's time:",presentTime)