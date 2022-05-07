'''Write a program in Python to perform the following operator based task: 
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication If User Enter 5 - Average
--Ask user to enter two numbers and keep those numbers in variables num1 
and num2 respectively for the first 4 options mentioned above.
--Ask the user to enter two more numbers as first and second for 
calculating the average as soon as the user chooses an option 5.
--At the end if the answer of any operation is Negative 
print a statement saying “NEGATIVE” 
NOTE: At a time a user can only perform one action.'''

print("Choose from the following option: ")
print(" Enter 1 for Addition")
print(" Enter 2 for Subtraction")
print(" Enter 3 for Division")
print(" Enter 4 for Multiplication")
print(" Enter 5 for Average")
num = int(input("Enter number between 1 and 5: "))
if str(num) in list("12345"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the Second number: "))
    if num == 1:
        result = num1 + num2 
        print("Sum of {} and {} is {}".format(num1, num2, result))
    if num == 2:
        result = num1 - num2 
        print("Difference of {} and {} is {}".format(num1, num2, result))
    if num == 3:
        result = num1/num2
        print("Division of {} by {} is {}".format(num1, num2, result))
    if num == 4:
        result = num1*num2
        print("Product of {} and {} is {}".format(num1, num2, result))
    if num == 5:
        first = int(input("Enter the third number: "))
        second = int(input("Enter the fourth number: "))
        result = (num1 + num2 +first + second)/4
        print("The average of {}, {}, {} and {} is : {} "
        .format(num1, num2, first, second, result))   
else:
    print("Enter a valid number between 1 and 5")
if result < 0:
    print("Negative")

