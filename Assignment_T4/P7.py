'''Define a function that can accept two strings as input and 
print the string with the maximum length in the console. 
If two strings have the same length, then the function should 
print both the strings line by line.'''

#funciton taking two strings and printing one with maximum length
#and if both having same length print both of them one by one
def str_length(str1, str2):
    if (len(str1) > len(str2)):
        print(str1)
    elif (len(str2) > len(str1)):
        print(str2)
    else:
        print(str1 , str2, sep = "\n")

#asking user to enter two strings
string_1 = input("Enter first string: ")
string_2 = input("Enter second string: " )
#calling function str_length
str_length(string_1, string_2)

