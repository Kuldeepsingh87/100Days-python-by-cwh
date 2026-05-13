#python lists
marks = [2,3,4]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

#list index
colors = ["red","green","blue","silver"]
print(colors[0])
print(colors[1])
print(colors[2])

#negative indexing
marks = [1,2,3,4]
print(marks[-3])
print(marks[len(marks)-3])

#list comprehension
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)