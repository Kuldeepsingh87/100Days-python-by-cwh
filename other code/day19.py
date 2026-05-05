#break and continue statement in python

#break statement
for i in range(12):
    print("5 X", i+1, "=", 5 * (i+1))
    if (i == 10):
        break
print("loop exit")

#continue statement
for i in range(12):
    if(i == 10):
        print("skip the iteration")
        continue
    print("5 X", i, "=",5 * i)