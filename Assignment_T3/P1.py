"""Create a list of 10 elements of four different data types 
like int, string, complex and float."""

#List creation by asking input from the user

list_1 = []
print("Enter 10 elements of data types int, string, complex and float: ")
for i in range(10):
    item = eval(input(" > "))
    list_1.append(item)
    if i == 9:
        print("Well done, list is ready..!")
print(f"List is: {list_1}")



