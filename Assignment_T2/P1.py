'''Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - 
Python Training” as a string.'''

# Asking user to enter a number of int type
number = int(input("Enter a number: "))
# checking if number is divisible by both 3 and 5
if (number % 3 == 0 and number % 5 == 0):
    print("Consultadd - Python Training")
#checking if number is only divisible by 3
elif (number % 3 == 0):
    print("Consultadd")
#checking if number is only divisible by 5
elif (number % 5 == 0):
    print("Python Training")

