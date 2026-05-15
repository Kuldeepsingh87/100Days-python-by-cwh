#dictionaries in python
dic = {
    344: "sudhanshu",
    345: "kumar",
    346: "verma",
    347: "deepanshu",
}
print(dic[344])

#accessing dictionary items using get method
info = {
    'name': "kuldeep",'age': "20", 'city': "almora"}
print(info)
print(info['name'])
print(info.get('eligible'))

#accessing multiple items from a dictionary using get method
info = {
    'name': "kuldeep",'age': "20", 'city': "almora"}
print(info.get('name', 'Not Found'))
print(info.get('eligible', 'Not Found'))


#accessing keys and values from a dictionar
info = {
    'name': "kuldeep",'age': "20", 'city': "almora"}
print(info.keys())#returns a view object that displays a list of all the keys in the dictionary
print(info.values())#returns a view object that displays a list of all the values in the dictionary
print(info.items())#returns a view object that displays a list of dictionary's key-value tuple pairs