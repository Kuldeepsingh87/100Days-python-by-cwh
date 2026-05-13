#sets in python
s = {2,4,2,6,8,4,10}
print(s)#not give duplicate values
s.add(12)#add new element in set
print(s)
s.remove(4)#remove element from set
print(s)
s.discard(6)#remove element from set
print(s)
s.clear()#remove all element from set
print(s)

#accessing set elements
#using for loop
info = {"name":"john", "age":30, "city":"new york"}
for item in info:
    print(item, ":", info[item])
