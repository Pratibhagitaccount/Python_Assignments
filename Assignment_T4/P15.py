'''Write a program in Python to multiply the elements of a list by itself 
using a traditional function and pass the function to map() to complete 
the operation.'''

def multiply (number):
    return(number*number)
list_1 = [1,2,3,4,5]
l = (list(map(multiply, list_1)))
print(f"New list is: {l}")