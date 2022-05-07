#Write a program to check the data type of the entered values.
'''HINT: Printed output should say - The data type of the input value is : 
int/float/string/etc'''

entered_value = eval(input("Enter a value of any type: "))
print("The data type of the input value is : {}" 
.format(type(entered_value)))
    

