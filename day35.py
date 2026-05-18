#for loop with else in python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

for i in range(6):
    print(i)
    if i == 3:
        break
else:
    print("Loop completed successfully")