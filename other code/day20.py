#python functions

#geometricmean function
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)

a = 9
b = 8
calculateGmean(a,b)

c = 8
d = 7
calculateGmean(c,d)

#for if else condition 
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)

a = 9
b = 8
if(a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")
calculateGmean(a,b)

c = 8
d = 74
if(c>d):
    print("first number is greater")
else:
    print("second number is greater or equal")
calculateGmean(c,d)

#for isgreater or islesser
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)

def isGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

def isLesser(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

a = 9
b = 8
isGreater(a,b)
calculateGmean(a,b)