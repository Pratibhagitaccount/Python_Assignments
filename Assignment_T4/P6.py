'''Define a function that can receive two integral numbers in string form and 
compute their sum and print it in the console.'''

#sum is a function that take two integral numbers in string form and compute their sum 
def sum (str1, str2):
    return(int(str1)+ int(str2))

#asking user to enter two integral numbers in string form
string_1 = input("Enter first numeric value: ")
string_2 = input("Enter second numeric value: ")
#calling function sum and storing its return in result
result = sum(string_1, string_2)
print(f"Sum of two numbers is: {result}")