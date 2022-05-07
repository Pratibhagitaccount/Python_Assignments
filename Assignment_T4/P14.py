'''Write a program in Python to find the values which are not divisible by 3 
but are a multiple of 7.
Make sure to use only higher order functions.'''

def check_number (num):
    if (num % 3 != 0) and (num % 7 == 0):
        return(num)

n = int(input("Enter the final limit to which we need to check: "))
print(" The values between 1 and 100, whcih are not divisible by 3, but are a multiple of 7: ")

#using user-defined function check_number
l = ((filter(check_number, range(1,n+1))))
print(f"Using user-defined function:\n {(list(l))}")

#using lambda function
m = filter(lambda x : (x % 3 != 0) and (x % 7 == 0), range(1, n))
print(f"Using Lambda function:\n {(list(m))}")
