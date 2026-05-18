#dictionary metods in python
ep1 = {
    'name': "kuldeep",
    'age': "20",
    'city': "almora"
}
#update method in dictionary
ep1.update({'name': "sudhanshu"})
print(ep1)
#clear method in dictionary
ep1.clear()
print(ep1)

#pop method in dictionary
ep1 = {
    'name': "kuldeep",
    'age': "20",
    'city': "almora"
}
ep1.pop('age')
print(ep1)

#delete method in dictionary
ep1 = {
    'name': "kuldeep",
    'age': "20",
    'city': "almora"
}

del ep1['age']
print(ep1)


