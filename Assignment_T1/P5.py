'''Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers 
and keep the sum in another variable called z. Add 30 to z and store the 
output in variable result and print result as the final output.'''

n1 = int(input("Enter Ist number between 1-10: "))
n2 = int(input("Enter 2nd number between 1-10: "))
z = n1 + n2
result = z + 30
print("Final output is: {}".format(result))