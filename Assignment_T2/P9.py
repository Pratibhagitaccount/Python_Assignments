'''Read the two parts of the question below:
Write a program such that it asks users to “guess the lucky number”. 
If the correct number is guessed the program stops, otherwise it continues 
forever.'''

# lucky_number = 45
# number = int(input("Guess the lucky number: "))
# while (True):
#     if number == lucky_number:
#         print("Hurray")
#         break
#     else:
#         number = int(input("Guess Again...:"))
#         continue
    
'''Modify the program so that it asks users whether they want to guess 
again each time. Use two variables, ‘number’ for the number and ‘answer’ 
for the answer to the question whether they want to continue guessing. 
The program stops if the user guesses the correct number or answers “no”. 
( The program continues as long as a user has not answered “no” and has 
not guessed the correct number)'''

lucky_number = 45
number = int(input("Enter the lucky number: "))
while True:
    if lucky_number == number:
        print("Hurray..!")
        break
    else:
        answer = input(" Enter 'Yes' to continue finding and 'No' to stop guessing: ").casefold()
        if answer == "yes":
            number = int(input("Guess again..: "))
            continue
        elif (answer == "no"):
            print("See you again..!")
            break
        












