"""Write a program which accepts a sequence of comma-separated numbers 
from console and generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)"""

import sys
# sys.argv[1] is the second parameter to be entered on the console:
list_1 = (sys.argv[1].split(","))
print(list_1)
print(tuple(list_1))
