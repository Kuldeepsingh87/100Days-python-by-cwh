#if-else statements
a = int(input("enter your age: "))
print("your age is:",a)

if(a>18):
    print("you can drive")#SPACE:indentation
else:
    print("you cannot drive")

#conditional statements
# >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

#if--else-python
appleprice = 220
budget = 200
if(appleprice <= budget):
    print("alexa, add 1 kg apples to the cart.")
else:
    print("alexa,do not add apples to the cart.")

#elif-python
num = int(input("enter the number: "))
if (num < 0):
    print("number is negative.")
elif(num == 0):
    print("number is zero.")
else:
    print("number is positive.")

#nested python
num = 18
if(num < 0):
    print("number is negative.")
elif (num > 0):
    if (num <= 10):
        print("number is btw 11-20")
    elif (num > 10 and num <= 20):
        print("number is btw 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")
