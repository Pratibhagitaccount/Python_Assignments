'''Write a program to replace the last element in a list with another list. 
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]'''

list_1 = [1,3,5,7,9,10]
list_2 = [2,4,6,8]
#removing last element of the list_1
list_1.pop()
#adding elements of list_2 in list_1
list_1.extend(list_2)
#output list is:
print(f"Expected output list is: {list_1}")