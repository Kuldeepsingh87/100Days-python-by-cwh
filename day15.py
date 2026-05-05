time = int(input("enter time in hours (0-23): "))

if 5 <= time < 12:
    print("good morning")
elif 12 <= time < 17:
    print("good afternoon")
elif 17 <= time < 21:
    print("good evening")
elif 21 <= time <= 23 or 0 <= time < 5:
    print ("good night")
else:
    print("invalid time entered!")