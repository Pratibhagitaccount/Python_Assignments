"""Write a program to get the sum and multiply of all the items in a 
   given list."""

list_1 = [1,2,3,4,5]
sum = 0
product = 1
for item in list_1:
    sum += item
    product *= item
print(f"sum and product of all elements of the list_1, {list_1} are: {sum}, {product}")


