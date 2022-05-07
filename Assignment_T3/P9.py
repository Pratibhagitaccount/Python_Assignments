'''Create a dictionary that contain numbers in the form(x:x*x) 
where x takes all the values between 1 and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}'''

#Enter a number upto which the value of dictionay is required
n = int(input("Enter the number: "))
# Dictionary using dict comprehension
dict_1 = {i :i*i for i in range (1, n+1)}
print(dict_1)
# Using for loop
for i in range (1, n+1):
    dict_1[i] = i*i
print(dict_1)

