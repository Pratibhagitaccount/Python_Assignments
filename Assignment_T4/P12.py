#Write a function to compute 5/0 and use try/except to catch the exceptions

numerator = int(input("Enter the value of numerator: "))
denominator = int(input("Enter the value of denominator: "))
try:
    result = numerator/ denominator
    print(result)    
except(ZeroDivisionError) as Z:
    print("Division by zero is not possible,",Z)
