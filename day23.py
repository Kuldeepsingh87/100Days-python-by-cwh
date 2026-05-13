#list.sort()
l = [1,2,4,6,3,5,11]
list.sort(l)
print(l)

#reverse()
l = [1,2,4,6,3,5,11]
list.reverse(l)
print(l)

#copy()
l = [1,2,4,6,3,5,11]
m = l.copy()
print(m)

#extend()
l = [1,2,4,6,3,5,11]
m = [100,200,240,500]
l.extend(m)
print(l)

#concatenate two list
l = [1,2,4,6,3,5,11]
m = [100,200,240,500]
k = l + m
print(k)