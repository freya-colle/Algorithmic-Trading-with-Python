"""
Types of Object
(1) Number
(2) String
(3) Logical Operations and Boolean
(4) Variable assignment
(5) Tuples and List
(6) Dictionary
(7) Set
"""
### TUPLES AND LISTS
a = float(input('mean = ',))
b= float(input('average = ',))
mean_average_couple = (a, b) #TUPLE ()
print(mean_average_couple)
my_list = [2, 3, 4, 5]
print(my_list)
my_list.append([a, b]) #add ONE value
print('add 1 value to list USING my_list.append(a): ',my_list) #NESTED LIST
print('Get the 1st element of the last element of my_list: ',my_list[-1][0])
my_list.extend([a, b]) # add MORE values
print('add more value to list using my_list.extend([a, b]): ', my_list)
my_list[0] #indexing
del my_list[0] #delete value
print('my_list after deleting the 1st value: ', my_list)

### DICTIONARY
diction9 = {'Vietcombank price': 50000}
diction9['TPB price:'] = 20000
print(diction9)
print('Get all the keys: ',diction9.keys())
print('Get all values: ',diction9.values())

###SET
set9 = {'price', 'avg_price', 2, 3}
print('Before add: ', set9)
set9.add(22)
print('After add: ',set9)
list2 = [1, 2, 3]
set(list2)
print('After change from list to set - set(list2): ',list2)