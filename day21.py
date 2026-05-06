#default arguments
def average (a=9,b=1):
    print("the average is",(a+b)/2)
average(7,1)

#keyword arguments
def average (a=9,b=1):
    print("the average is",(a+b)/2)
average(b=54,a=26)

#required arguments
def average (a,b,c=5):
    print("the average is ",(a+b+c)/2)
average(8,7)

#keyword arbitary arguments
def average (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is:", sum / len(numbers))
average(5,6,7,1)

#return statements
def average (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
c = average(5,6,7,1)
print(c)