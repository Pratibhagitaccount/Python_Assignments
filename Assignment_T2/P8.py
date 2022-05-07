'''Write a program that accepts a string as an input from the user 
and calculate the number of digits and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2'''

count_letters = 0
count_digits = 0
string = input("Enter a string: ").casefold()
for char in string:
    if char.isalpha():
        count_letters += 1
    if char.isnumeric():
        count_digits += 1
print("In the given string: {} \n Number of digits are: {} \n Number of letters are: {}" 
.format(string, count_digits, count_letters))      
    