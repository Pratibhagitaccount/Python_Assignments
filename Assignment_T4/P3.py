'''Create a function that takes a list and returns a new list with 
unique elements of the first list.'''

list_1 = [1,2,3,4,2,3,4,5]
list_2 = []
#using for loop
for item in list_1:
    if item not in list_2:
        list_2.append(item)
print(list_2)
#using type-casting
set_1 = set(list_1)
print(set_1)
print(list(set_1))