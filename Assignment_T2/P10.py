lucky_number = 45
number = int(input("Guess a luckynumber: "))
count = 0
while count < 5:
    count+=1
    if (lucky_number == number):
        print("Good Guess!")
        break
    elif(count == 5):
        print("Game Over!")
        break
    else:
        number = int(input("Try again! "))
        continue
