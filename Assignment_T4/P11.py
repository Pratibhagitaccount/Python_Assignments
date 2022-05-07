'''Write a program which uses map() and filter() to make a list whose elements 
are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].'''

list_1 = [1,2,3,4,5,6,7,8,9,10]
#to filter out even elements from the list
list_2 = list(filter(lambda x : x%2==0, list_1))
# to square the elements of list_2
list_3 = list(map(lambda x : x*x, list_2 ))
print(list_3)