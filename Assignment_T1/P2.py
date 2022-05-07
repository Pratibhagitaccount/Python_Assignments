'''Create a variable of type complex and swap it with another variable of 
type integer.'''

a_complex = 4+3j
a_int = 10
print("The values of a_complex and a_int before swap are: {}, {}"
.format(a_complex, a_int))
a_mid = a_complex
a_complex = a_int
a_int = a_mid
print("The values of a_complex and a_int after swap are: {}, {}"
.format(a_complex, a_int))
