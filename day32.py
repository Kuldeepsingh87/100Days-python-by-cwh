#joining sets
s1 = {1,2,3}
s2 = {4,5,6}
print(s1.union(s2))#join two sets
print(s1|s2)#join two sets
s1.update(s2)#join two sets and update the first set
print(s1)

#union and update
cities1 = {"New York", "Los Angeles", "Chicago"}
cities2 = {"Houston", "Phoenix", "Philadelphia"}
cities3 = cities1.union(cities2)
print(cities3)

#intersection and update = A*B = {x | x in A and x in B}
cities = {"New York", "Los Angeles", "Chicago"} #intersection of cities and cities2 will be "Los Angeles" because it is the only common element
cities2 = {"Los Angeles", "Houston", "Phoenix"} #intersection = check for common elements between two sets
cities.intersection_update(cities2)
print(cities)

#symetric difference = (A-B) U (B-A) and update 
# A*B = (A-B) U (B-A)
cities1 = {"New York", "Los Angeles", "Chicago"}
cities2 = {"Los Angeles", "Houston", "Phoenix"}
cities3 = cities1.symmetric_difference(cities2) 
print(cities3)   

#difference and update
cities1 = {"New York", "Los Angeles", "Chicago"}
cities2 = {"Los Angeles", "Houston", "Phoenix"}
cities3 = cities1.difference(cities2)
print(cities3)

#itdisjoint set = check if two sets have no common elements
cities1 = {"New York", "Los Angeles", "Chicago"}
cities2 = {"Houston", "Phoenix", "Philadelphia"}
print(cities1.isdisjoint(cities2))#true because there are no common elements

#issuperset = check if a set contains all elements of another set
cities1 = {"New York", "Los Angeles", "Chicago"}
cities2 = {"Los Angeles", "Chicago"}    
print(cities1.issuperset(cities2))#true because cities1 contains all elements of cities2

#issubset = check if a set is a subset of another set
cities1 = {"New York", "Los Angeles", "Chicago"}
cities2 = {"Los Angeles", "Chicago"}    
print(cities2.issubset(cities1))#true because cities2 is a subset of cities1

#adding elements to a set
cities = {"New York", "Los Angeles", "Chicago"}
cities.add("Houston")#add one element to a set
print(cities)

#updateing a set with multiple elements
cities = {"New York", "Los Angeles", "Chicago"} 
cities.update(["Houston", "Phoenix", "Philadelphia"])#add multiple elements to a set
print(cities)   

#removing elements from a set
cities = {"New York", "Los Angeles", "Chicago", "Houston"}
cities.remove("Houston")#remove an element from a set
print(cities)


#discarding elements from a set
cities = {"New York", "Los Angeles", "Chicago", "Houston"}
cities.discard("Houston")#remove an element from a set, but does not raise an
#error if the element is not found
print(cities)

#popping an element from a set
cities = {"New York", "Los Angeles", "Chicago", "Houston"}
popped_city = cities.pop()#remove and return an arbitrary element from a set
print(popped_city)
print(cities)

#deleting a set
cities = {"New York", "Los Angeles", "Chicago", "Houston"}
del cities#delete a set
print(cities)#this will raise an error because the set has been deleted

#clearing a set
cities = {"New York", "Los Angeles", "Chicago", "Houston"}
cities.clear()#remove all elements from a set
print(cities)#this will print an empty set

#check if item exists in a set
cities = {"New York", "Los Angeles", "Chicago", "Houston"}
print("New York" in cities)#true because "New York" is in the set

