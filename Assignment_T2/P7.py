"""Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement"""

for num in range(0,6):
    if num == 3:
        continue
    print(num, end = " ")