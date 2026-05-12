#exercise 2 solution
import time 
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print (hour)

if (hour>=0 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<17):
    print("Good Afternoon!")
elif(hour>0 and hour<=12):
    print("Good Evening!")