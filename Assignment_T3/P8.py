'''Create a new dictionary by concatenating the following two dictionaries: 
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}'''

a = {1:10, 2:20}
b = {3:30, 4:40}
#Concatenation using .update method
a.update(b)
print(a)
#concatenation using for loop
for key, value in b.items():
    a[key] = value

print(a)