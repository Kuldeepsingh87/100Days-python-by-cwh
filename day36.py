#exception handling in python
a = input("Enter a number: ")
print(f"multiplication table of {a}:")

for i in range(1, 11):
    print(f"{int(a)} x {i} = {int(a) * i}")