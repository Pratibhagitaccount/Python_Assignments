"""If one data type value is assigned to ‘a’ variable and then a 
different data type value is assigned to ‘a’ again.
 Will it change the value? If Yes then Why?"""

#Assigning int to variable a
a = 23
print(a)
#Assigning float to same variable a
a = 2.3
print(a)


""" In Python, same variable can be reassigned to objects of different 
types, as varaibles in Pyhton donot store the values directly, they work 
as to point the objects in memory. As we can see in above example, firstly
a is pointing to the integer object with value 23, and then it is pointing
to float object with value 2.3 in it."""