#operations on tuples

#manipulating tuples
fruits = ("apple","banana","mango","grapes","papaya")
temp = list(fruits)
temp.append("pineapple") #add item
temp.pop(2) #remove item
temp[4] = "watermelon" #change item
fruits = tuple(temp)
print(fruits)

#count()method
tuple1 = (1,2,3,4,5,6,7,8,9,1,2,3)
res = tuple1.count(3)
print('count of 3 in tuple1 is:',res)

#index()method
tuple2 = (1,2,6,4,5,3,7,8,9,1,2,3)
res = tuple2.index(3)
print('index of 3 in tuple2 is:',res)