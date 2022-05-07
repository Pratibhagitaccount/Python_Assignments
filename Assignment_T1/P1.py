"""Create three variables in a single line and assign values to them in 
such a manner that each one of them belongs to a different data type.
E.g. :
a = 1,
b = 2.01,
c = 'string'"""

#Defining a, b & c with different data types in one line
a, b, c = 1, 2.01, 'string'
#Printing the values of a, b and c
print(" The values of a, b and c are: {}, {} and {} respectively."
.format(a, b, c))
#Printing the types of a, b, & c
print(" The datatypes of a, b and c are: {}, {} and {} respectively."
.format(type(a), type(b), type(c)))

