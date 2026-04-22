#operators
#arithmetic operators
print(15+6)#addition
print(15-6)#subtraction
print(15*6)#multiplication
print(15**6)#exponential
print(15/6)#division 
print(15%6)#modulus
print(15//6)#floor division

#exercise
n = 15
m = 7
ans1 = n+m 
print("addition of",n,"and",m,"is",ans1)
ans2 = n-m
print("subtraction of",n,"and",m,"is",ans2)
ans3 = n*m
print("multiplication of",n,"and",m,"is",ans3)
ans4 = n/m
print("division of",n,"and",m,"is",ans4)
ans5 = n%m
print("modulus of",n,"and",m,"is",ans5)
ans6 = n//m
print("floor division of",n,"and",m,"is",ans6)


#creating a calculator
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))

addition = num1 + num2
multiplication = num1 * num2
subtraction = num1 - num2

if num2 != 0:
    division = num1/num2
else:
    division = "Undefined (cannot divide by zero)"

    print("\n------ Calculator Results ------")
print(f"First Number  : {num1}")
print(f"Second Number : {num2}")
print("--------------------------------")
print(f"Addition       : {num1} + {num2} = {addition}")
print(f"Subtraction    : {num1} - {num2} = {subtraction}")
print(f"Multiplication : {num1} * {num2} = {multiplication}")
print(f"Division       : {num1} / {num2} = {division}")
print("--------------------------------")