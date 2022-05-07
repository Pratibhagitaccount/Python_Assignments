'''Define a function which can generate and print a tuple where the 
values are square of numbers between 1 and 20 (both 1 and 20 included).'''

#using list comprehenstion, to generate a list with squares of numbers 
# between 1 and 20
list_1 = [x*x for x in range(1,21)]
#printing the tuple of same using typecasting
print(f"Tuple of square of 1 to 20: \n{tuple(list_1)}")