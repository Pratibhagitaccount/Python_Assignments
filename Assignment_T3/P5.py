"""Create a new list which contains the specified numbers after removing 
the even numbers from a predefined list."""

#defining list_1
list_1 = [1,2,3,4,5,6,7,8]
#for loop to remove even elements from the list
for item in list_1:
    if item %2 == 0:
        list_1.remove(item)
print(f"List_1, after removing even elements, becomes {list_1}")

