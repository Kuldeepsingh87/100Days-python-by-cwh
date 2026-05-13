#recursion in python
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num - 1)
num = 7;
print("number:", num)
print("factorial:", factorial(num))