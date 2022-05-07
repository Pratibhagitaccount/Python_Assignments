"""Swap two numbers using a third variable and do the same task 
without using any third variable."""

# Defining variables x and y
x = 20
y = 40 
print("Values of x and y before swapping are: {}, {}"
.format(x, y))

# Swap using third variable
z = x
x = y 
y = z
print("Values of x and y after swapping using third variable are: {}, {}"
.format(x, y))

#Swap without using third variable
x, y = y, x
print("Values of x and y after swapping again without using third varaible are: {}, {}" 
.format(x, y))




