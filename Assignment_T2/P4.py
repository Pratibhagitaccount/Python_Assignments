'''Write a program in Python to break and continue if the following 
cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and 
print “Good Going” '''

while True:
    number = int(input("Enter a number greater or less than 0: "))
    if number > 0:
        print("Good Going")
        continue
    elif number < 0:
        print("Its Over")
        break
    else:
        print("Invalid number")


