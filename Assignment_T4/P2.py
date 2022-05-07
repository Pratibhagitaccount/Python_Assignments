'''Write a function that accepts a string and prints the number of uppercase 
letters and lowercase letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 
No. of Lower case Characters : 12'''

string = input("Enter the string with lower and uppercase charachter: ")
upper_count = 0
lower_count = 0
for char in string:
    if char.isupper(): 
        upper_count+=1
    else:
        lower_count+=1

print(f"No. of Uppercase characters: {upper_count} \nNo.of Lower case Characters: {lower_count}")