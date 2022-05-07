# x=123
# for i in x:
#     print(i)

'''This code will give us an error, as we cannot iterate over int object.'''


# i= 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break 
#     else:
#         print("error")

# " It will print: 
#                 0
#                 error
#                 1
#                 error
#                 2
'''as when i becomes 3, it break out of the loop, because of break keyword 
under i == 3 statement." '''

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
"""output is 0
             1
             2
             3
             4 
          as when it prints 4, count becomes 5, with count +=1 statement, and 
conditon count = 5, satisfies and it breaks out of loop."""











