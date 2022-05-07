"""Write a program in Python which will find all such numbers 
which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200."""

#For loop to access element between 2000 and 3200
for item in range(2000, 3201):
    #To check whether item is divisible by 7 and not a multiple of 5
    if item % 7 == 0 and item % 5 != 0:
        print(item, end = ", ")

    