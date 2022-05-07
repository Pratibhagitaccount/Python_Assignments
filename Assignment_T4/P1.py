'''Write a program to reverse a string. 
Sample input: “1234abcd” 
Expected output: “dcba4321” '''

string = input("Enter a string to be reversed: ")
#using for loop:
for i in range(len(string)):
    print(string[len(string)-1-i], end = "")

#using slicing method
print("\n",string[::-1])

