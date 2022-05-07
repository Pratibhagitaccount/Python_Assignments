'''Write a program that accepts a hyphen-separated sequence of words as input 
and prints the words in a hyphen-separated sequence after sorting them
 alphabetically.'''

string = input("Enter hyphen-seprated sequence fo words: ")
#spliting the string with "-"
string1 = string.split("-")
#sorting by words
string1.sort()
#joining the sorted string with "-"
print("-".join(string1))
